#######################################################
# Script permettant de transférer un dataset vers une #
# autre plateforme open data ODS.                     #
# Nécessite des droits d'admin sur les 2 portails     #
# Le jeu transféré peut être supprimé à la fin        #
# du traitement en fonction du paramétrage.           #
#######################################################

from odsapimanagement import apikey
from cOdMEL import cOdMEL as odMEL

from transfertList import transfertPagesList  # Get all datasets to be transfered

import os

#################################################
#################################################
def main():
    for page in transfertPagesList:
        print("Traitement de la page : {}".format(page))
        transfertPage(page)


def transfertPage(page):

    apiKeyOrigine = apikey  # for testing while the test domain is not available
    urlFrom = "YOUR URL"  # for testing while the test domain is not available

    # Identifiants du portail source
    od = odMEL(apiKeyOrigine, True)
    # od.changeUrl(urlFrom)

    # Identifiants du portail de destination (par défaut : opendata.lillemetropole.fr)
    apikeyTest = "YOUR API KEY"  # MasterKey Dev
    od_dest = odMEL(apikeyTest, True)
    od_dest.changeUrl(urlFrom)

    #################################################
    # Récupération de la page
    req, pageInfos = od.retrievePage(page)

    if req:
        pageInfos.pop("pushed_by_parent", None)
        pageInfos.pop("has_subdomain_copies", None)
        pageInfos.pop("created_at", None)
        pageInfos.pop("last_modified", None)
        pageInfos.pop("last_modified_user", None)
        pageInfos.pop("author", None)
        od_dest.createPage(pageInfos)
    # print(pageInfos)
    print("Fini !!")


if __name__ == "__main__":
    main()
