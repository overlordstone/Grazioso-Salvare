# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
from pymongo import MongoClient

class AnimalShelterCRUD:
    def __init__(self):
        mongo_user = os.environ.get('MONGO_USER', 'aacuser')
        mongo_pass = os.environ.get('MONGO_PASS', 'MySnhu')
        mongo_host = os.environ.get('MONGO_HOST', 'nv-desktop-services.apporto.com')
        mongo_port = int(os.environ.get('MONGO_PORT', 30055))

        self.client = MongoClient(host=mongo_host, port=mongo_port, username=mongo_user, password=mongo_pass, authSource='admin')
        self.db = self.client['AAC']
        self.collection = self.db['animals']

    def insert_animal(self, name, species, age, shelter):
        try:
            animal_data = {'name': name, 'species': species, 'age': age, 'shelter': shelter}
            result = self.collection.insert_one(animal_data)
            return True if result.inserted_id else False
        except Exception as e:
            print(f"Error inserting animal document: {e}")
            return False

    def query_animals(self, query):
        try:
            cursor = self.collection.find(query)
            result_list = [animal for animal in cursor]
            return result_list
        except Exception as e:
            print(f"Error querying animal documents: {e}")
            return []

    def update_animals(self, query, update_data):
        try:
            result = self.collection.update_many(query, {'$set': update_data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating animal documents: {e}")
            return 0

    def delete_animals(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting animal documents: {e}")
            return 0

# Example usage:
# animal_shelter = AnimalShelterCRUD()
# data = {"name": "Fluffy", "species": "Cat", "age": 5, "shelter": "Example Shelter"}
# success = animal_shelter.insert_animal(**data)
# if success:
#     print("Document inserted successfully.")
# else:
#     print("Failed to insert document.")
# documents = animal_shelter.query_animals({"species": "Cat"})
# print(documents)
# num_updated = animal_shelter.update_animals({"species": "Cat"}, {"age": 6})
# print(f"Number of documents updated: {num_updated}")
# num_deleted = animal_shelter.delete_animals({"species": "Cat"})
# print(f"Number of documents deleted: {num_deleted}")




