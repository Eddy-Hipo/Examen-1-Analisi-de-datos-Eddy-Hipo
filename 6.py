from argparse import ArgumentParser
import requests
import pymongo 
from pymongo.errors import ConnectionFailure
from bson import json_util, ObjectId
import couchdb
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

#Conexion a couchDb
URL = 'http://Admin:Admin@localhost:5984'
try:
    response = requests.get(URL)
    if response.status_code == 200:
        print('CouchDB connection: Success')
    if response.status_code == 401:
        print('CouchDB connection: failed', response.json())
except requests.ConnectionError as e:
    raise e

server=couchdb.Server(URL)

nombredb='mongocouchexamen'
try: 
    dbcouch=server.create(nombredb)
except: 
    dbcouch=server[nombredb]



for db in DBS:
    if db in ('examen'):  
        cols = CLIENT[db].list_collection_names() 
        for col in cols:
            print('Querying documents from collection {} in database {}'.format(col, db))
            for x in CLIENT[db][col].find():  
                try:
                    documents = json.loads(json_util.dumps(x))
                    dbcouch.save(documents)
                    print("SAVE")
                    print(documents)
                except:
                    print("This document already exist")