#######################################################
# Script permettant de transférer un dataset vers une #
# autre plateforme open data ODS.                     #
# Nécessite des droits d'admin sur les 2 portails     #
# Le jeu transféré peut être supprimé à la fin        #
# du traitement en fonction du paramétrage.           #
#######################################################

from transfertParam import od, od_dest

from transfertList import transfertDtList  # Get all datasets to be transfered

import os

#################################################
#################################################
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("OD")
print(od)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("OD dest")
print(od_dest)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#################################################
def main():
    for dt in transfertDtList:
        print("Traitement du dataset : {}".format(dt))
        transfert(dt)


def transfert(dt):
    dataset = dt
    datasetDest = dataset

    #################################################
    # Récupération des données du dataset
    dtId = od.getDatasetUid(dataset)

    ## Lister les ressources
    print("##########################")
    print("Récupération des ressources")
    ressources = od.getAllResources(dtId)
    ### Gestion des ressources fichier
    for res in ressources:
        if res["url"][:10] == "odsfile://":
            od.downloadFile(res["title"].lower())

    ## Lister métadonnées
    print("##########################")
    print("Récupération des métadonnées")
    metadonneesCatalog = od.getAllMetadata(dtId)
    allMetadonnees = []
    for meta in metadonneesCatalog:
        metaVal = od.getMetadata(dtId, meta["template"]["name"], meta["name"])
        if metaVal is not None:
            # le champs modifié a un format datetime qui ne passe pas quand on le recharge,
            # comme il ne sert pas à grand chose dans notre cas, on le vire
            if meta["name"] != "modified":
                allMetadonnees.append(
                    {
                        "template_name": meta["template"]["name"],
                        "metadata_name": meta["name"],
                        "override_remote_value": False,
                        "value": metaVal,
                    }
                )

    ## Lister pièces jointes
    print("##########################")
    print("Récupération des pièces jointes")
    listAtt = od.listAttachments(dtId)
    for att in listAtt:
        print(
            "Téléchargement de {} : ".format(att["attachment_uid"]),
            od.downloadAttachment(
                dtId, att["attachment_uid"], att["url"][10:]
            ),  # [10:] pour virer odsfile://
        )

    ## Lister exports alternatifs
    print("##########################")
    print("Récupération des exports alternatifs")
    listAE = od.listAlternativeExports(dtId)
    for ae in listAE:
        print(
            "Téléchargement de {} : ".format(ae["export_uid"]),
            od.downloadAlternativeExport(
                dtId, ae["export_uid"], ae["url"][10:]
            ),  # [10:] pour virer odsfile://
        )

    ## Lister processeurs
    print("##########################")
    print("Récupération des processeurs")
    listProc = od.getDatasetProcessor(dtId)

    ## Lister les fields specifications
    print("##########################")
    print("Récupération des fields specifications")
    listFieldsSpec = od.getDatasetFieldsSpecifications(dtId)

    ## Lister règles de sécurité
    print("##########################")
    print("Sécurité Groupe")
    listGroupSecurity = od.getGroups(dtId)
    print(listGroupSecurity)
    print("##########################")
    print("Sécurité utilisateurs")
    listUserSecurity = od.getUserSecurity(dtId)
    print(listUserSecurity)

    #################################################
    # Vérifier existence du dataset sur autre instance
    print("##########################")
    print("Vérification si le jeu existe")
    dtExist = False
    try:
        dtIdDest = od_dest.getDatasetUid(datasetDest)
        if type(dtIdDest) != type(0):
            dtExist = True
    except Exception as error:
        print(error)

    #################################################
    ## Créer dataset
    if dtExist == False:
        print("##########################")
        print("Création du dataset")

        dtDest = od_dest.createDataset(datasetDest, {})
        dtIdDest = dtDest["dataset_uid"]
        datasetDest = dtDest["dataset_id"]

    ## charger les ressources fichiers
    ## créer les ressources
    print("##########################")
    print("Chargement des ressources")
    for resource in ressources:
        # upload des fichiers
        if res["url"][:10] == "odsfile://":
            ret = od_dest.uploadFile(os.path.join("dl", res["title"].lower()))
            if type(ret) != type(False):
                print("L'upload de {} semble être ok".format(res["title"].lower()))
            resource["url"] = ret["url"]

        # Clean resource fields before adding it
        resource.pop("resource_uid", None)
        resource.pop("resource_id", None)
        resource.pop("dataset", None)
        resource.pop("last_modified", None)
        # print(resource)
        od_dest.addRessource(dtIdDest, resource)

    ## charger métadonnées
    print("##########################")
    print("Chargement des métadonnées")
    od_dest.setMultipleMetadata(dtIdDest, allMetadonnees)

    ## Si PJ et Exports Alternatifs, charger fichiers
    ## puis créer les PJ et EA
    print("##########################")
    print("Chargement des pièces jointes")
    for pj in listAtt:
        file = od_dest.uploadFile(os.path.join("dl", pj["url"][10:]))
        od_dest.addAttachment(dtIdDest, file["url"])

    print("##########################")
    print("Chargement des exports alternatifs")
    for ae in listAE:
        file = od_dest.uploadFile(os.path.join("dl", ae["url"][10:]))
        od_dest.addAlternativeExport(dtIdDest, file["url"])

    ## Créer les processeurs
    print("##########################")
    print("Chargement des processeurs")
    for proc in listProc:
        od_dest.setProcessor(dtIdDest, proc["name"], proc["args"])

    ## Paramétrer les fields specifications
    print("##########################")
    print("Chargement des fields specification")
    for fieldSpec in listFieldsSpec:
        fieldSpec.pop("processor_uid", None)
        od_dest.setDatasetFieldsSpecifications(dtIdDest, fieldSpec)

    ## Fixer les règles de sécurité
    print("##########################")
    print("Securité :")
    print("---------------------")
    print("Securité groupe")
    for lgs in listGroupSecurity:
        od_dest.setGroupData(dtIdDest, lgs)

    print("---------------------")
    print("Securité Utilisateur")
    for usd in listUserSecurity:
        od_dest.setUserSecurity(dtIdDest, usd)

    ## Publier le dataset
    print("##########################")
    print("Publier le dataset")
    od_dest.publishDataset(dtIdDest)

    #################################################
    # Voir si on supprime le jeu de donnée sur plateforme initiale

    print("Fini !!")


if __name__ == "__main__":
    main()
