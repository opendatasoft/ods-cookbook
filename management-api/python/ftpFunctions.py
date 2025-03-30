import ftplib
from dateutil import parser

############################################################################################
def getFilefromFTP(file, ftpAddr, ftpLogin, ftpPasswd, ftpDirectory=""):
    ftp = ftplib.FTP(ftpAddr)
    ftp.login(ftpLogin, ftpPasswd)
    if ftpDirectory != "":
        ftp.cwd(ftpDirectory)
    ftp.retrbinary("RETR {}".format(file), open(file, "wb").write)
    ftp.quit()


############################################################################################
def getGTFSfromFTP(ftpAddr, ftpLogin, ftpPasswd, ftpDirectory=""):
    """
    Récupère le GTFS depuis le FTP MEL et le télécharge sur la machine locale
    """

    getFilefromFTP("gtfs.zip", ftpAddr, ftpLogin, ftpPasswd, ftpDirectory)


############################################################################################
def getLastModifFTPfile(file, ftpAddr, ftpLogin, ftpPasswd, ftpDirectory=""):
    """
    Get last update of a file in a FTP server

    Parameters :
        file        :   File to get information
        ftpAddr     :   Address of the server
        ftpLogin    :   Login of the user
        ftpPasswd   :  Password of the user
        ftpDirectory:  Directory where is the file to check

    Returns :
        Last modification of the file
    """
    ftp = ftplib.FTP(ftpAddr)
    ftp.login(ftpLogin, ftpPasswd)
    ftp.cwd(ftpDirectory)

    dateFile = ftp.voidcmd("MDTM {}".format(file))[4:].strip()

    time = parser.parse(dateFile)

    return time
