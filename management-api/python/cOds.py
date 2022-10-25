import os
from fileinput import filename
import requests
import json
import getpass
import markdown

############################################################################################
class cOds:
    def __init__(self, url="https://data.opendatasoft.com/", apikey="", verif=True):

        if url[-1:] != "/":
            url += "/"

        self.__baseUrl = url
        self.__apikey = apikey
        self.__verif = verif

        self.setApiKey(apikey)

    ########################################################################################
    def __str__(self):
        return """Base url : {baseUrl}
Apikey : {apikey}
Verif ssl : {verif}""".format(
            baseUrl=self.__baseUrl, apikey=self.__apikey, verif=self.__verif
        )

    ########################################################################################
    ########################################################################################
    def setApiKey(self, apikey: str):
        if apikey != "":
            self.__header = {"Authorization": "Apikey {}".format(apikey)}
            self.__apikey = apikey
        else:
            self.__header = None

    ########################################################################################
    ########################################################################################
    def changeUrl(self, url):
        self.__baseUrl = url

    ########################################################################################
    ########################################################################################
    def makeGetRequest(self, request: str):
        """Make a GET request

        Args:
            request (str): Request to be passed

        Returns:
            bool: True / False if the request is ok or not
            obj: datas from the request or error message
        """

        try:
            r = requests.get(request, headers=self.__header, verify=self.__verif)

            if r.status_code == 200:
                datas = r.json()
                return True, datas
            else:
                print(r.status_code, r.text, sep="\n")
                return False, r.text
        except Exception as error:
            print(error)
            return False, error

    ########################################################################################
    def makePostRequest(self, request: str, payload: dict):
        """Make a POST request

        Args:
            request (str): Request to be sent
            payload (dict): Payload of the request

        Returns:
            _type_: _description_
        """
        r = requests.post(
            request,
            headers=self.__header,
            data=json.dumps(payload),
            verify=self.__verif,
        )

        if r.status_code == 200:
            datas = r.json()
            return datas
        else:
            print(r.status_code, r.text)
            return 0

    ########################################################################################
    def makePutRequest(self, request: str, payload: dict):
        r = requests.put(
            request, headers=self.__header, data=payload, verify=self.__verif
        )

        if r.status_code == 200:
            datas = r.json()
            return datas
        elif r.status_code == 204:
            return r.status_code
        else:
            print(r.status_code, r.text)
            return 0

    ########################################################################################
    def makeDeleteRequest(self, request: str):
        r = requests.delete(request, headers=self.__header, verify=self.__verif)

        if r.status_code == 200:
            datas = r.json()
            return datas
        elif r.status_code == 204:
            return r.status_code
        else:
            print(r.status_code, r.text)
            return r.status_code

    ########################################################################################
    ########################################################################################
    def publishDataset(self, datasetId: str):
        """
        Publie un jeu de données sur le portail ODS

        Parameters:
            datasetId   :   Identifiant unique du jeu de données

        Returns:
            0 si erreur
            Job object
        """
        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/publish"
        )

        r = requests.put(request, headers=self.__header, verify=self.__verif)

        if r.status_code == 200:
            datas = r.json()
            # print(datas)
            return 1, datas
        else:
            print(r.status_code, r.text)
            return 0, r.status_code

    ########################################################################################
    def publishMetadata(self, datasetId: str):  ## A TESTER !!!
        """
        Publie les métadatas d'un jeu de données sur le portail ODS

        Parameters:
            datasetId   :   Identifiant unique du jeu de données

        Returns:
            0 si erreur
            Job object
        """
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/publish_metadata"
        )

        r = requests.put(request, headers=self.__header, verify=self.__verif)

        if r.status_code == 200:
            datas = r.json()
            # print(datas)
            return 1, datas
        else:
            print(r.status_code, r.text)
            return 0, r.status_code

    ########################################################################################
    def abortProcessing(self, datasetId: str):
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/abort_processing"
        )

        self.makePutRequest(request, None)

    ########################################################################################
    def getDataset(self, datasetName: str, start=0, rows=10, parameters=""):
        """Get a dataset

        Parameters:
        datasetName (string): Name of the dataset you want te retrieve
        start (int): Index of the first item to return (starting at 0). Default: 0
        rows (int): Number of items to return. Default: 10
        parameters (string): list of parameters URL encoded. ex : param1=value1&param2=value2. Default: ""

        Returns:
        total_count (int): Number of elements in the catalog
        datasets (list): list of all datasets
        parameters (list) : list of parameters
        """

        request = (
            self.__baseUrl
            + "api/records/1.0/search/?dataset="
            + datasetName
            + "&rows="
            + str(rows)
            + "&start="
            + str(start)
            + "&"
            + parameters
        )

        reqOk, respJson = self.makeGetRequest(request)

        if reqOk:
            return respJson["nhits"], respJson["records"], respJson["parameters"]
        else:
            return 0, 0, 0

    ########################################################################################
    def createDataset(self, datasetId, metas):
        payload = {"dataset_id": datasetId, "metas": metas}
        datas = json.dumps(payload)

        # Construction de la requete
        request = self.__baseUrl + "api/management/v2/datasets/"

        res = self.makePostRequest(request, payload)
        # print(res)
        return res

    ########################################################################################
    def getAllResources(self, datasetId: str):
        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/resources"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            # print("Resources : ", datas, sep="\n")
            return datas
        else:
            print(datas)
            return 0

    ########################################################################################
    def addRessource(self, datasetId: str, payload: dict):
        """
        Ajoute une ressource à un jeu de donnée.
        The payload must be a valid resource object without any uid.

        Parameters:
            datasetId   :   Identifiant unique du dataset
            urlFile     :   url du fichier à mettre en ressource. Doit être de type odsfile

        Returns:
            0 si erreur
            Objet Resource : https://help.opendatasoft.com/management-api/#the-resource-object
        """
        # payload sample
        # { "url": "odsfile://resource.csv", "title": "My Awesome Data File", "type": "csvfile", "params": {"headers_first_row": false, "separator": ";"}}

        datas = json.dumps(payload)

        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/resources"
        )

        res = self.makePostRequest(request, payload)
        print(res)

        # r = requests.post(request, headers=self.__header, data=datas)

        # if r.status_code == 200:
        #    datas = r.json()
        #    print("Add resource", datas, sep="\n")
        #    return datas
        # else:
        #    print(
        #        "Erreur ajout de la ressource", r.status_code, r.text, sep="\n"
        #    )
        #    return 0

    ########################################################################################
    def getDatasetHarvester(self, harvester: str):
        """Get all dataset retrieved by an ODS harverster

        Args:
            harvester (str): Name of the harvester

        Returns:
            obj: List of the dataset / False if error
        """
        # https://opendata.lillemetropole.fr/api/datasets/1.0/search/?refine.publishing.harvester=Isog%C3%A9o%20MEL&staged=true&rows=-1
        request = (
            self.__baseUrl
            + "api/datasets/1.0/search/?refine.publishing.harvester={}&staged=true&rows=-1".format(
                harvester
            )
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas["datasets"]
        else:
            return False

    ########################################################################################
    def getDatasetFromPublisher(self, publisher: str):
        """Get all dataset retrieved by a publisher

        Args:
            harvester (str): Name of the harvester

        Returns:
            obj: List of the dataset / False if error
        """

        request = (
            self.__baseUrl
            + "api/datasets/1.0/search/?refine.publisher={}&staged=false&rows=-1".format(
                publisher
            )
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas["datasets"]
        else:
            return False

    ########################################################################################
    def getODSdatas(self, nbRows=50):
        """Get all datasets from open data site

        Args:
            nbRows (int, optional): Number of rows return by API call. Defaults to 50.

        Returns:
            list: List of all datasets
        """

        nbDatasets, datas, params = self.getDataset("domaindatasets", rows=nbRows)
        print("Nombre datasets : ", nbDatasets)
        if nbDatasets > nbRows:
            i = nbRows
            while i < nbDatasets:
                print("Start :", i)
                nb, loopDatas, params = self.getDataset(
                    "domaindatasets", start=i, rows=nbRows
                )
                datas += loopDatas
                i += nbRows

        return datas

    ########################################################################################
    def getDatasetUid(self, datasetName: str):
        """Get the unique id from a dataset

        Parameters:
            datasetName (str) :   identifiant du jeu de données

        Returns:
            Identifiant unique du dataset
            0 si erreur
        """
        request = self.__baseUrl + "api/v2/catalog/datasets/" + datasetName

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas["dataset"]["dataset_uid"]
        else:
            print(
                "Erreur dans la requête d'appel de l'identifiant unique",
                request,
                datas,
                sep="\n####################################################\n",
            )
            return 0

    ########################################################################################
    def addAPIkey(self, nameKey: str, login="", passwd=""):
        """
        Ajoute une clé API pour un utilisateur
        Par défaut, les droits sont à "Voir les jeux restreints"

        Parameters:
            namekey :   Nom de la clé qu'on veut créer

        Returns:
            Clé créée
            0 si erreur
        """
        payload = {"label": nameKey, "permissions": ["edit_dataset"]}
        datas = json.dumps(payload)

        request = self.__baseUrl + "api/management/v2/apikeys/"

        if login == "":
            login = input("Entrer le login admin : ")
        if passwd == "":
            passwd = getpass.getpass(prompt="Mot de passe pour {} : ".format(login))

        r = requests.post(request, auth=(login, passwd), data=datas)

        if r.status_code == 200:
            print(r.text)
            return r
        else:
            print(r.status_code, r.text)
            return 0

    ########################################################################################
    def setAllPrivilegeAPIkey(
        self, apikey: str, keyName="MasterKey", login="", passwd=""
    ):
        """
        Accorde tous les privilèges à un utilisateur donné
        Besoin d'un compte admin

        Parameters:
            apikey  :   Clé API à modifier
            keyName (str, optional) : Name of the key. Default MasterKey
        """
        payload = {
            "label": keyName,
            "permissions": [
                "edit_domain",
                "create_page",
                "edit_page",
                "manage_page",
                "explore_restricted_page",
                "create_dataset",
                "edit_dataset",
                "publish_dataset",
                "manage_dataset",
                "explore_restricted_dataset",
                "edit_reuse",
                "manage_subdomains",
                "explore_monitoring",
                "edit_theme",
            ],
        }

        datas = json.dumps(payload)

        request = self.__baseUrl + "api/management/v2/apikeys/" + apikey

        if login == "":
            login = input("Entrer le login admin : ")
        if passwd == "":
            passwd = getpass.getpass(prompt="Mot de passe pour {} : ".format(login))

        r = requests.put(request, auth=(login, passwd), data=datas)

        if r.status_code == 200:
            print(r.text)
            return True
        else:
            print(r.status_code, r.text)
            return False

    ########################################################################################
    def listAttachments(self, datasetId: str):
        """
        Affiche la liste des pièces jointes d'un jeu de données

        Parameters:
            datasetId   :   Identifiant unique du dataset

        Returns:
            0 si erreur
            Objet avec les pièces jointes si tout va bien
        """
        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/attachments"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            # print("Attachments", datas, sep="\n")
            return datas
        else:
            print(datas)
            return 0

    ########################################################################################
    def addAttachment(self, datasetId: str, urlFile: str):
        """
        Ajoute une export pièce jointe à un jeu de donnée

        Parameters:
            datasetId   :   Identifiant unique du dataset
            urlFile     :   url du fichier à mettre en pièce jointe. Doit être de type odsfile

        Returns:
            0 si erreur
            Objet Attachment : https://help.opendatasoft.com/management-api/#the-attachment-object
        """
        payload = {"url": urlFile}
        datas = json.dumps(payload)

        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/attachments"
        )

        r = requests.post(request, headers=self.__header, data=datas)

        if r.status_code == 200:
            datas = r.json()
            # print("Add attachment", datas, sep="\n")
            return datas
        else:
            print("Erreur ajout de la pièce jointe", r.status_code, r.text, sep="\n")
            return 0

    ########################################################################################
    def deleteAttachment(self, idDataset: str, idAttachment: str):
        """
        Supprime un export alternatif d'un dataset Opendatasoft
        /!\ Ne supprime pas le fichier depuis le serveur ODS

        Parameters:
            idDataset    :   Idetifiant unique du dataset
            idAttachment :   Identifiant unique de la pièce jointe

        Returns:
            1 si tout va bien
            0 sinon
        """
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + idDataset
            + "/attachments/"
            + idAttachment
        )

        r = requests.delete(request, headers=self.__header)

        if r.status_code == 200:
            return 1
        else:
            print("Erreur dans la requête de suppression")
            return 0

    ########################################################################################
    def downloadAttachment(self, idDataset: str, idAttachment: str, fileName: str):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + idDataset
            + "/download_attachment/"
            + idAttachment
        )

        try:
            r = requests.get(request, headers=self.__header, verify=self.__verif)

            if r.status_code == 200:
                attachment_data = r.content

                # save to file
                with open(os.path.join("dl", fileName), "wb") as f:
                    f.write(attachment_data)
                    f.close()
                    return True
            else:
                print(r.status_code, r.text)
                return False
        except Exception as error:
            print(error)
            return False

    ########################################################################################
    def listAlternativeExports(self, datasetId: str):
        """
        Affiche la liste des exports alternatifs d'un jeu de données

        Parameters:
            datasetId   :   Identifiant unique du dataset

        Returns:
            0 si erreur
            Objet avec les exports alternatifs si tout va bien
        """
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/alternative_exports"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            # print("Alternatives exports", datas, sep="\n")
            return datas
        else:
            print(datas)
            return 0

    ########################################################################################
    def addAlternativeExport(self, datasetId: str, urlFile: str):
        """
        Ajoute un export alternatif à un jeu de donnée

        Parameters:
            datasetId   :   Identifiant unique du dataset
            urlFile     :   url du fichier à mettre en export alternatif. Doit être de type odsfile

        Returns:
            0 si erreur
            Objet Alternative export : https://help.opendatasoft.com/management-api/#the-alternative-export-object
        """
        payload = {"url": urlFile}
        datas = json.dumps(payload)

        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/alternative_exports"
        )

        r = requests.post(request, headers=self.__header, data=datas)

        if r.status_code == 200:
            datas = r.json()
            # print("Add alternative export", datas, sep="\n")
            return datas
        else:
            print(
                "Erreur ajout de l'export alternatif", r.status_code, r.text, sep="\n"
            )
            return 0

    ########################################################################################
    def deleteAlternativeExport(self, idDataset: str, idAltExport: str):
        """
        Supprime un export alternatif d'un dataset Opendatasoft
        /!\ Ne supprime pas le fichier depuis le serveur ODS

        Parameters:
            idDataset   :   Idetifiant unique du dataset
            idAltExport :   Identifiant unique de l'export alternatif

        Returns:
            1 si tout va bien
            0 sinon
        """
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + idDataset
            + "/alternative_exports/"
            + idAltExport
        )

        r = requests.delete(request, headers=self.__header)

        if r.status_code == 200:
            return 1
        else:
            print("Erreur dans la requête de suppression")
            return 0

    ########################################################################################
    def downloadAlternativeExport(
        self, idDataset: str, idAltExport: str, fileName: str
    ):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + idDataset
            + "/download_alternative_export/"
            + idAltExport
        )

        try:
            r = requests.get(request, headers=self.__header, verify=self.__verif)

            if r.status_code == 200:
                attachment_data = r.content

                # save to file
                with open(os.path.join("dl", fileName), "wb") as f:
                    f.write(attachment_data)
                    f.close()
                    return True
            else:
                print(r.status_code, r.text)
                return False
        except Exception as error:
            print(error)
            return False

    ########################################################################################
    def sendZipFileToOds(self, filename: str):
        """
        Envoie un fichier local vers le portail ODS
        """
        # payload = {
        #    "mimetype": "application/zip",
        #    "filename": filename,
        #    "file": filename,
        #    "is_alternative_export": True,
        # }
        # datas = json.dumps(payload)

        file = {"file": (filename, open(filename, "rb"))}

        # Construction de la requete
        request = self.__baseUrl + "api/management/v2/files"

        r = requests.post(
            request, headers=self.__header, files=file, verify=self.__verif
        )

        if r.status_code == 200:
            datas = r.json()
            print(datas)
            return datas["url"]
        else:
            print(r.status_code, r.text)
            return 0

    ########################################################################################
    def getDescriptionMetadata(self, datasetId: str):
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/metadata/default/description"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            if datas["value"] == None:
                return datas["remote_value"]
            else:
                return datas["value"]

    ########################################################################################
    def setDescriptionMetadata(self, datasetId: str, descText: str):
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/metadata/default/description"
        )

        payload = {
            "value": descText,
            "override_remote_value": "true",
        }
        datas = json.dumps(payload)

        r = requests.put(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        if r.status_code == 200:
            # print("Ok", r.text, sep="\n")
            return 1
        else:
            return 0

    ########################################################################################
    def getAllMetadata(self, datasetId: str):
        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/metadata/"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas
        else:
            return []

    ########################################################################################
    def getMetadata(self, datasetId: str, metaType: str, metaDataWanted: str):
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/metadata/{metaType}/{metaWanted}".format(
                metaType=metaType, metaWanted=metaDataWanted
            )
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            if datas["value"] == None:
                return datas["remote_value"]
            else:
                return datas["value"]

    ########################################################################################
    def setMetadata(self, datasetId, value, metaType, metaDataWanted):
        # Construction de la requete
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/metadata/{metaType}/{metaWanted}".format(
                metaType=metaType, metaWanted=metaDataWanted
            )
        )

        payload = {
            "value": value,
            "override_remote_value": "true",
        }
        datas = json.dumps(payload)

        r = requests.put(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        if r.status_code == 200:
            return 1
        else:
            return 0

    ########################################################################################
    def setMultipleMetadata(self, datasetId, metadatas):
        # Construction de la requete
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/metadata/"
        )

        payload = {"metas": metadatas}

        self.makePutRequest(request, json.dumps(payload))

    ########################################################################################

    def changePublisherName(self, oldPublisher, newPublisher):
        datasets = self.getDatasetFromPublisher(oldPublisher)

        ligne = 1
        lenDatasets = len(datasets)
        for dataset in datasets:
            dtId = self.getDatasetUid(dataset["datasetid"])
            print(
                "Traitement de ligne {}/{} | ".format(ligne, lenDatasets),
                dataset["metas"]["title"],
            )
            ligne += 1
            self.setMetadata(
                dtId,
                newPublisher,
                "default",
                "publisher",
            )
            # self.publishDataset(dtId)
            self.publishMetadata(dtId)

    ########################################################################################
    def changeInfoMarkdownToHTML(self, datasetId: str):
        txtMarkDown = self.getDescriptionMetadata(datasetId)

        ret = self.setDescriptionMetadata(datasetId, markdown.markdown(txtMarkDown))
        # self.publishDataset(datasetId)
        self.publishMetadata(datasetId)

        return ret

    ########################################################################################
    def getDatasetFieldsSpecifications(self, datasetId: str):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/fields_specifications/"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas
        else:
            return False

    ########################################################################################
    def setDatasetFieldsSpecifications(self, datasetId: str, payload: dict):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/fields_specifications/"
        )

        return self.makePostRequest(request, payload)

    ########################################################################################
    def updtDatasetFieldsSpecifications(self, datasetId: str, fsId: str, payload: dict):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/fields_specifications/"
            + fsId
        )

        print(request)

        return self.makePutRequest(request, payload)

    ########################################################################################
    def getDatasetProcessor(self, datasetId: str):
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/processors/"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas
        else:
            return False

    ########################################################################################
    def setProcessor(self, datasetId: str, processorName: str, args):
        request = (
            self.__baseUrl + "api/management/v2/datasets/" + datasetId + "/processors/"
        )

        payload = {
            "name": processorName,
            "args": args,
        }
        datas = json.dumps(payload)

        # print(datas)

        r = requests.post(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        # print(r.status_code, r.text)

        if r.status_code == 200:
            return 1
        else:
            return 0

    ########################################################################################
    def updateProcessor(
        self, datasetId: str, processorId: str, label: str, processorName: str, args
    ):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/processors/"
            + processorId
        )

        payload = {"name": processorName, "args": args, "label": label}
        datas = json.dumps(payload)

        print(datas)

        r = requests.put(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        # print(r.status_code, r.text)

        if r.status_code == 200:
            return 1
        else:
            print(r.status_code, r.reason)
            return 0

    ########################################################################################
    def getAvailableProcessor(self):
        request = self.__baseUrl + "api/management/v2/processors/"

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas
        else:
            return False

    ########################################################################################
    def guessProcessor(self, datasetId: str, processorName: str):
        """Retrieve possible processor parameters from processor name

        Args:
            datasetId (str): _description_
            processorName (str): _description_

        Returns:
            _type_: _description_
        """
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/guess_processor_params/"
        )

        payload = {"name": processorName}
        datas = json.dumps(payload)

        print(datas)

        r = requests.post(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        print(r.status_code, r.text)

        if r.status_code == 200:
            return 1

    ########################################################################################
    def getAllGroups(self):
        request = self.__baseUrl + "api/management/v2/groups/"

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return sorted(datas, key=lambda d: d["title"])

    ########################################################################################
    def getGroups(self, datasetId):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/security/groups/"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas

    ########################################################################################
    def setGroup(self, datasetId: str, groupId: str):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/security/groups/"
        )

        payload = {
            "group": {"group_id": groupId},
            "is_data_visible": False,
            "visible_fields": ["*"],
            "filter_query": "",
            "api_calls_quota": None,
            "permissions": [
                "explore_restricted_dataset",
                "edit_dataset",
                "publish_dataset",
            ],
        }
        datas = json.dumps(payload)

        r = requests.post(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        if r.status_code == 200:
            return r.json()
        else:
            return r.json()

    ########################################################################################
    def setGroupData(self, datasetId: str, payload: dict):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/security/groups/"
        )

        datas = json.dumps(payload)

        r = requests.post(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        # print(request)
        # print(payload)
        # print("Ajout Sécurité Groupe :")
        # print(r.json())

        if r.status_code == 200:
            return r.json()
        else:
            return r.json()

    ########################################################################################
    def getUserSecurity(self, datasetId):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/security/users/"
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas

    ########################################################################################
    def giveUserAccess(self, datasetId: str, userName: str):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/security/users/"
        )

        payload = {
            "user": {"username": userName},
            "is_data_visible": False,
            "visible_fields": ["*"],
            "filter_query": "",
            "api_calls_quota": None,
            "permissions": [
                "explore_restricted_dataset",
                "edit_dataset",
                "publish_dataset",
            ],
        }
        datas = json.dumps(payload)

        r = requests.post(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        if r.status_code == 200:
            return r.json()
        else:
            return r.json()

    ########################################################################################
    def setUserSecurity(self, datasetId: str, payload: dict):
        request = (
            self.__baseUrl
            + "api/management/v2/datasets/"
            + datasetId
            + "/security/users/"
        )

        datas = json.dumps(payload)

        r = requests.post(
            request, headers=self.__header, data=datas, verify=self.__verif
        )

        # print(request)
        # print("Ajout Sécurité Utilisateur :")
        # print(r.json())

        if r.status_code == 200:
            return r.json()
        else:
            return r.json()

    ########################################################################################
    def getDatasetsFromTheme(self, theme: str):
        request = (
            self.__baseUrl
            + "api/datasets/1.0/search/?q=theme%3A%22{theme}%22&rows=-1".format(
                theme=theme
            )
        )

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            return datas["datasets"]

    ########################################################################################
    def getThemeUid(self, theme: str):
        return self.getUidFromListDt(self.getDatasetsFromTheme(theme))

    ########################################################################################
    def getUidFromPublisher(self, publisher: str) -> list:
        return self.getUidFromListDt(self.getDatasetFromPublisher(publisher))

    ########################################################################################
    def getUidFromListDt(self, listDt: list) -> list:
        listUid = []
        for item in listDt:
            listUid.append(self.getDatasetUid(item["datasetid"]))
        return listUid

    ########################################################################################
    ####  Pages  ###########################################################################
    ########################################################################################
    def deletePage(self, pageName: str):
        """Delete a page on a website

        Args:
            pageName (str): Slug from the page to delete
        """
        request = self.__baseUrl + "api/management/v2/pages/{PAGE_SLUG}".format(
            PAGE_SLUG=pageName
        )

        ret = self.makeDeleteRequest(request)

        return ret

    ########################################################################################
    def retrievePage(self, pageName: str):
        """Retrieve a page on a website

        Args:
            pageName (str): Slug from the page to retrieve
        """
        request = self.__baseUrl + "api/management/v2/pages/{PAGE_SLUG}".format(
            PAGE_SLUG=pageName
        )

        ret = self.makeGetRequest(request)

        return ret

    ########################################################################################
    def createPage(self, datas: dict):
        """Create a page on a website

        Args:
            pageName (str): Slug from the page to delete
        """
        request = self.__baseUrl + "api/management/v2/pages/"

        ret = self.makePostRequest(request, datas)

        return ret

    ########################################################################################
    ####  Users  ###########################################################################
    ########################################################################################
    def listUsers(self, rows=10, page=1):
        """Get the list of users

        Args:
            rows (int, optional): Number of line you want to retrieve by API call. Defaults to 10. -1 retrieve all users
            page (int, optional): Page number wanted. Defaults to 1.

        Returns:
            dict: The list of users
        """

        # Construction de la requete
        request = self.__baseUrl + "api/management/v2/users/?rows={}&page={}".format(
            rows, page
        )
        if rows == -1:
            request = self.__baseUrl + "api/management/v2/users/?rows=1&page=1"

        reqOk, datas = self.makeGetRequest(request)

        if reqOk:
            if rows == -1:
                nbHits = datas["nhits"]
                getBy = 70
                page = 1
                allUsers = []
                while (page - 1) * getBy < nbHits:
                    print("on est là. {}".format(page))
                    allUsers += self.listUsers(getBy, page)
                    page += 1
                return allUsers
            else:
                return datas["users"]
        else:
            print(datas)
            return 0

    ########################################################################################
    def getListUsers(self, page=0, size=20):
        if page == 0:
            pageAsk = 1
        else:
            pageAsk = page

        request = (
            self.__baseUrl
            + "api/management/v2/users?rows={rows}&page={page}".format(
                rows=size, page=pageAsk
            )
        )

        reqOk, ret = self.makeGetRequest(request)

        if reqOk == True:
            nhits = ret["nhits"]

            datasUsers = ret["users"]

            if page == 0:
                if nhits > size:
                    i = pageAsk + 1
                    while i * size < nhits + size:
                        print("Page :", i)
                        nb, loopDatas = self.getListUsers(page=i, size=size)
                        datasUsers += loopDatas
                        i += 1
        else:
            nhits = 0
            datasUsers = []
        return nhits, datasUsers

    ########################################################################################
    def deleteUser(self, username: str):

        request = self.__baseUrl + "api/management/v2/users/{username}".format(
            username=username
        )

        return self.makeDeleteRequest(request)

    ########################################################################################
    def getAppelParUserLastMonths(self, dureeJour=60):
        request = (
            self.__baseUrl
            + "api/v2/monitoring/datasets/ods-api-monitoring/records?select=user_id%2Ccount(*)%20as%20nb_appels_api&where=timestamp%3Enow(days%3D-{duree})&group_by=user_id&sort=nb_appels_api%20DESC&limit=100&pretty=false&timezone=UTC".format(
                duree=dureeJour
            )
        )

        reqOk, ret = self.makeGetRequest(request)
        if reqOk:
            appels = []
            for record in ret["records"]:
                # print(record["record"]["fields"])
                appels.append(record["record"]["fields"])
            return appels

    ########################################################################################
    def deleteFile(self, fileName: str):
        request = self.__baseUrl + "api/management/v2/download_file/{FILE_ID}".format(
            FILE_ID=fileName
        )

        # Fonction non supportée pour le moment
        # self.makeDeleteRequest(request)
        print("Fonction non supportée pour le moment !")

    ########################################################################################
    def downloadFile(self, fileName: str):
        request = self.__baseUrl + "api/management/v2/download_file/{FILE_ID}".format(
            FILE_ID=fileName
        )

        try:
            r = requests.get(request, headers=self.__header, verify=self.__verif)

            if r.status_code == 200:
                attachment_data = r.content

                # save to file
                with open(os.path.join("dl", fileName), "wb") as f:
                    f.write(attachment_data)
                    f.close()
                    return True
            else:
                print(r.status_code, r.text)
                return False
        except Exception as error:
            print(error)
            return False

    ########################################################################################
    def uploadFile(self, fileName: str):
        request = self.__baseUrl + "api/management/v2/files"

        # print("File name : ", fileName)
        file = {"file": (fileName, open(fileName, "rb"))}

        r = requests.post(
            request, headers=self.__header, verify=self.__verif, files=file
        )

        if r.status_code == 200:
            return r.json()
        else:
            print("Erreur d'upload de fichier")
            print(r.text)
            return False

    ########################################################################################
    ########################################################################################
