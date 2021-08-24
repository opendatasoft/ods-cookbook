# coding: utf-8

import requests
import json

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ApiError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message=""):
        self.expression = expression
        self.message = message

######################################################################
######################################################################

'''Class to call ODS Portail API in your code
'''
class readODS:
    """ Init your class
        
    Parameters:
    url (string): URL of the ODS Portail you want to call. URL has to finish by a / Default: "https://data.opendatasoft.com/"
    apiKey (string): An API key to make identified calls or call restricted dataset. Default: ""

    """

    def __init__(self, url="https://data.opendatasoft.com/", apiKey=""):
        self.url = url
        self.apikey = apiKey

    def getDataset(self, datasetName, start=0, rows=10, parameters = ""):
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

        request = self.url + "api/records/1.0/search/?dataset=" + datasetName + "&rows=" + str(rows) + "&start=" + str(start) + "&" + parameters
        if self.apikey != "":
            request = request + "&apikey=" + self.apikey
                    
        respJson = self.makeRequest(request)
        
        return respJson["nhits"], respJson["records"], respJson["parameters"]
    
    def getCatalog(self, start=0, rows=10):
        """Get catalog info
        
        Parameters:
        start (int): Index of the first item to return (starting at 0). Default: 0
        rows (int): Number of items to return. Default: 10 
        
        Returns:
        total_count (int): Number of elements in the catalog
        datasets (list): list of all datasets
        """
        request = self.url + "api/v2/catalog/datasets?rows=" + str(rows) + "&start=" + str(start)
        if self.apikey != "":
            request = request + "&apikey=" + self.apikey
                    
        respJson = self.makeRequest(request)
        
        return respJson["total_count"], respJson["datasets"]
    
    def getCatalogMonitoring(self):
        """Get monitoring datasets info
        
        Parameters:
        None
        
        Returns:
        total_count (int): Number of elements in the catalog
        datasets (list): list of all datasets
        """
        request = self.url + "api/v2/monitoring/datasets"
        if self.apikey != "":
            request = request + "?apikey=" + self.apikey
                    
        respJson = self.makeRequest(request)
        
        return respJson["total_count"], respJson["datasets"]
    
    def makeRequest(self, request):
        
        try:
            resp = requests.get(request)
            if resp.status_code != 200:
                # error
                raise ApiError('GET {}'.format(resp.status_code), request)
        except ApiError:
            print("Erreur dans l'appel de l'API")
            raise
            
        respJson = resp.json()
        
        return respJson

######################################################################
