from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import *
from statistics import mean


class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista: Motorista):
        try:
            res = self.db.collection.insert_one(vars(motorista))
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"An error occurred while creating motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"====== Motorista encontrado ======")
            return res
        except Exception as e:
            print(f"An error occurred while reading motorista: {e}")
            return None

    def update_motorista(self, id: str, corridas):
        try:
            ''' Atualizando nota média do motorista '''
            motorista = self.db.collection.find_one({"_id": ObjectId(id)})
            motorista['corridas'].extend(corridas)
            notas = [x['nota'] for x in motorista['corridas']]
            media = sum(notas) // len(notas)
            motorista['nota'] = media

            ''' Inserindo novas corridas '''
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {'$set': motorista})

            print(f"Motorista atualizados: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"An error occurred while updating motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"motorista deleted: {res.deleted_count} document(s) deleted")
            return res.deleted_count
        except Exception as e:
            print(f"An error occurred while deleting motorista: {e}")
            return None

