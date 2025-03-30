#######################################################
#                                                     #
# Liste des paramètres pour la migration des datasets #
#                                                     #
#######################################################
from odsapimanagement import apikey
from cOdMEL import cOdMEL as odMEL

# Source
apikeyDev = "YOUR KEY"  # MasterKey Dev
urlDev = "YOUR URL"  # for testing while the test domain is not available

# Identifiants du portail source
global od
od = odMEL(apikeyDev, True)
od.changeUrl(urlDev)

# Destination (par défaut : opendata.lillemetropole.fr)
od_dest = odMEL(apikey, True)
