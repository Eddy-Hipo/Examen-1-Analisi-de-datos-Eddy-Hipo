import sqlite3 as sq
import pandas as pd
import json
from pymongo import MongoClient
con=sq.connect("sqlexamen.db") #La base de datos debe existir y estar en la misma carpeta del documento
dfsqlite=pd.read_sql_query("SELECT * FROM compras",con)
result = dfsqlite.to_json(orient ="records")
parsed=json.loads(result)

MONGO_HOST = 'mongodb://localhost/examen'
for post in parsed:
    try:
        client = MongoClient(MONGO_HOST)
        db = client.examen         
        db.SQLiteamongo.insert_one(post)
        print("Dato guardado")
    except Exception as e:    
        print("no se pudo guardar:" + str(e))