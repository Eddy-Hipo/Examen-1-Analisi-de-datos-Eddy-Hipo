from argparse import ArgumentParser
import requests
import pymongo 
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
import dns
import json

#Conexion a mongodb

CLIENT = pymongo.MongoClient('mongodb://localhost:27017')#Indicarparametrosdel servidor

try:
    CLIENT.admin.command('ismaster')
    print('MongoDB connection: Success')
except ConnectionFailure as cf:
    print('MongoDB connection: failed', cf)

#SeleccionarSchema
DBS = ['examen']


#Conexion a mongodb Atlas
SERVER = MongoClient("mongodb+srv://esfot:esfot@cluster0.n9mge.mongodb.net/examen?retryWrites=true&w=majority")

try:
    SERVER.admin.command('ismaster')
    print('MongoDB Atlas connection: Success')
except ConnectionFailure as cf:
    print('MongoDB Atlas connection: failed', cf)
    
DBSA = SERVER.get_database('examen')
dbsCollectionA = DBSA.mongoamongoatlas

for db in DBS:
    if db in ('examen'):  
        cols = CLIENT[db].list_collection_names() 
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    dbsCollectionA.insert_one(documents)
                    print("SAVE")
                    print(documents)
                except:
                    print("This document already exist")