# ods_python

A python package to get ODS information

**class readODS**
   Init your class
       
   _Parameters:_
   url (string): URL of the ODS Portail you want to call. URL has to finish by a / Default: "https://data.opendatasoft.com/"
   apiKey (string): An API key to make identified calls or call restricted dataset. Default: ""
   
   Methods defined here:
   
   \_\_init\_\_(self, url='https://data.opendatasoft.com/', apiKey='')
       Initialize self.  See help(type(self)) for accurate signature.
   
   **getCatalog**(self, start=0, rows=10)
       Get catalog info
       
       Parameters:
       start (int): Index of the first item to return (starting at 0). Default: 0
       rows (int): Number of items to return. Default: 10
       
       Returns:
       total_count (int): Number of elements in the catalog
       datasets (list): list of all datasets
   
   **getCatalogMonitoring**(self)
       Get monitoring datasets info
       
       Parameters:
       None
       
       Returns:
       total_count (int): Number of elements in the catalog
       datasets (list): list of all datasets
   
   **getDataset**(self, datasetName, start=0, rows=10, parameters='')
       Get a dataset
       
       Parameters:
       datasetName (string): Name of the dataset you want te retrieve
       start (int): Index of the first item to return (starting at 0). Default: 0
       rows (int): Number of items to return. Default: 10 
       parameters (string): list of parameters URL encoded. ex : param1=value1&param2=value2. Default: ""
       
       Returns:
       total_count (int): Number of elements in the catalog
       datasets (list): list of all datasets
       parameters (list) : list of parameters
   
   **makeRequest**(self, request)
       Don't use this function. Called by other functions of the class
       Make the request on the ODS website
 