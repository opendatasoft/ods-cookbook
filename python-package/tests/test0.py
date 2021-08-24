from ods_python import ods_python

portailMEL = readODS("http://opendata.lillemetropole.fr/")

print(portailMEL.getCatalog())
print(portailMEL.getCatalogMonitoring())
ret = portailMEL.getDataset("vlille-realtime")
print(type(ret))
print(ret)