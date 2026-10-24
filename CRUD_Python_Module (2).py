# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password, host, port, DB, col): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        username = 'aacuser' 
        PASS = 'DarthBruce' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}') 
        self.database = self.client[DB] 
        self.collection = self.database[COL] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            result= self.collection.insert_one(data)
            return True if result.acknowledged else False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    
    def read(self, search_data=None):
        if search_data is None:
            search_data = {}
            
        result = self.collection.find(search_data)  
        
        return list(result)
    
    # update
    
    def update(self, query, update_data):
        if query is not None and update_data is not None:
            result = self.collection.update_many(query, update_data)
            
            return result.modified_count
        else: raise Exception("Update failed: query and update_data parameters not provided")
        
    #delete
    
    def delete(self, query):
        if query is not None:
            
            result = self.collection.delete_many(query)
            
            return result.deleted_count
        
        else:
            raise Exception("Delete failed: query cannot be empty")
            
