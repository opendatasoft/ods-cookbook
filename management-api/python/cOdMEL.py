from cOds import cOds as ods
from datetime import datetime, timedelta
from progress.bar import Bar
import pandas as pd

########################################################################################


class cOdMEL(ods):
    def __init__(self, apikey="", verif=True):
        """Initialize cOdMEL object.
        URL is known, just pass an API key to make API Management

        Args:
            apikey (str, optional): Give an API key with management rights. Defaults to "".
            verif (bool, optional): Set if verification on SSL must be activated. Defaults to True.
        """
        super().__init__("https://opendata.lillemetropole.fr/", apikey, verif)

        self.setApiKey(apikey)

    ########################################################################################
    def supprimerUtilisateurNonActives(self, nbMonth=3):
        """Delete users which did not active their account since X months. By default 3 months.

        Args:
            nbMonth (int, optional): Number of months. Defaults to 3.
        """
        now = datetime.now()
        month = timedelta(days=30)

        nhits, users = self.getListUsers()
        print("Nombre d'utilisateurs en base : ", nhits, len(users))
        count = 0
        for user in users:
            if user["is_active"] == False:
                user["date_joined"] = datetime.strptime(
                    user["date_joined"][:-6], "%Y-%m-%dT%H:%M:%S"
                )
                if (now - user["date_joined"]) // month > nbMonth:
                    if self.deleteUser(user["username"]) == 204:
                        print("Utilisateur {} supprimé".format(user["username"]))
                        count += 1
        print("{} comptes ont été supprimés".format(count))

        return count

    ########################################################################################
    def changeUrlIsogeo(self):
        # Get allDatasets from harvester
        datas = self.getDatasetHarvester("Isogéo MEL")

        with Bar(
            "Traitement des jeux de données en cours",
            max=len(datas),
        ) as bar:
            for data in datas:
                try:
                    dtId = self.getDatasetUid(data["datasetid"])

                    if type(dtId) != type(0):
                        datasetRef = self.getMetadata(dtId, "default", "references")
                        # check if the url has ever been modified
                        if datasetRef[8:12] != "open":
                            datasetRef = self.TraiteUrlIsogeo(datasetRef)
                            self.setMetadata(dtId, datasetRef, "default", "references")
                            # self.publishDataset(dtId)
                            self.publishMetadata(dtId)

                except Exception as error:
                    print(error)

                bar.next()
            bar.finish()

    ########################################################################################
    def TraiteUrlIsogeo(self, urlIsogeo: str) -> str:
        """Transform an isogeo url into a new url

        Args:
            urlIsogeo (str): URL with XML datas

        Returns:
            str: URL open isogeo
        """
        splitted = urlIsogeo.split("/")

        lastParam = splitted[8].split("?")
        urlFinale = (
            "https://open.isogeo.com/s/" + splitted[5] + "/" + lastParam[0] + "/r/"
        )

        lastParam = lastParam[1].split("%3A")[4].split("&")[0].replace("-", "")
        urlFinale += lastParam

        return urlFinale

    ########################################################################################
    def getInactiveAccounts(self, inactiveTime=3, nbDayApiCall=360):
        """Get a list of account which have not been actived since a given time

        Args:
            inactiveTime (int): Number of year since last seen
            nbDayApiCall (int): Number of days since last API call

        Returns:
            list: List of users
        """
        now = datetime.now()
        month = timedelta(days=30)
        year = timedelta(days=365)

        countDelete = 0

        # Fetch list of users and list of API call from XX (param nbDayApiCall) last days
        nhits, listUsers = self.getListUsers()
        users = self.getAppelParUserLastMonths(nbDayApiCall)

        list_export = []

        # Fetch in user list if last seen is bigger than X (param inactiveTime) years and add it to a list
        for user in listUsers:
            if "last_seen" in user:
                if user["last_seen"] is not None:
                    user["last_seen"] = datetime.strptime(
                        user["last_seen"][:-6], "%Y-%m-%dT%H:%M:%S"
                    )
                    if now - user["last_seen"] > inactiveTime * year:
                        # check if user is an ODS member
                        if user["is_ods"] == False:
                            # check if user is in the list of user which made API call recently
                            if (
                                next(
                                    (
                                        item
                                        for item in users
                                        if item["user_id"] == user["username"]
                                    ),
                                    None,
                                )
                                is None
                            ):

                                # Add to list in order to make an export of the list
                                list_export.append(
                                    {
                                        "username": user["username"],
                                        "mail": user["email"],
                                        "last_seen": user["last_seen"].strftime(
                                            "%d/%m/%Y %H:%M:%S"
                                        ),
                                    }
                                )
                        else:
                            print(
                                "USER ODS",
                                user["username"],
                                user["email"],
                                user["last_seen"],
                            )
        return list_export

    ########################################################################################
    def deleteInactiveAccounts(
        self, inactiveTime=3, nbDayApiCall=360, fileName="erreurSuppr"
    ):
        """Delete accounts from inactives accounts
        An excel file of deleted accounts is created

         Args:
            inactiveTime (int): Number of year since last seen
            nbDayApiCall (int): Number of days since last API call
            fileName (str): Name of the excel file

        Returns:
            int: Number of deleted accounts
        """

        countDelete = 0

        # Fetch list of users and list of API call from XX (param nbDayApiCall) last days
        listUsers = self.getInactiveAccounts(inactiveTime, nbDayApiCall)

        list_error = []

        for user in listUsers:
            # Delete user
            retSuppr = self.deleteUser(user["username"])
            if retSuppr == 204:
                print("Utilisateur {} supprimé".format(user["username"]))
                countDelete += 1
            else:
                list_error.append(
                    {
                        "username": user["username"],
                        "mail": user["email"],
                        "last_seen": user["last_seen"].strftime("%d/%m/%Y %H:%M:%S"),
                        "error-code": retSuppr,
                    }
                )

        print("{} comptes ont été supprimés".format(countDelete))

        dfErrors = pd.DataFrame(list_error)
        writer = pd.ExcelWriter("{}.xlsx".format(fileName), engine="xlsxwriter")
        dfErrors.to_excel(writer, sheet_name="errors", index=False)
        writer.save()
        return countDelete

    ########################################################################################
    def setEpsg(self, dataset, epsg):
        """Set the good EPSG to a geometric field from a WFS"""
        dtid = self.getDatasetUid(dataset)

        # {"name": "string_extractor", "args": {"field": "text_field", "regexp": "(?P<planet>^World)"}
        if type(dtid) != type(0):
            epsg_geo_point_2d = {"source_epsg_code": epsg, "field": "geo_point_2d"}
            epsg_geo_shape = {"source_epsg_code": epsg, "field": "geo_shape"}

            r1 = self.setProcessor(dtid, "transform_coordinates", epsg_geo_point_2d)
            r2 = self.setProcessor(dtid, "transform_coordinates", epsg_geo_shape)
            if r1 and r2:
                # ods.publishDataset(dtid)
                self.publishMetadata(dtid)
        else:
            print("Dataset non reconnu")

    ########################################################################################
    def changeMarkDownToHtmlIsogeo(self, harversterName):
        """Set the description field of datasets harvested from Isogeo wich is by default in Markdown which is not supported by ODS"""
        datas = self.getDatasetHarvester(harversterName)

        with Bar(
            "Traitement des jeux de données en cours",
            max=len(datas),
        ) as bar:
            for data in datas:
                try:
                    dtId = self.getDatasetUid(data["datasetid"])
                    if type(dtId) != type(0):
                        self.changeInfoMarkdownToHTML(dtId)

                except Exception as error:
                    print(error)

                bar.next()
            bar.finish()

    ########################################################################################
    ########################################################################################
