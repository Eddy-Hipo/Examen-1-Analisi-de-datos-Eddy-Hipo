import json
import pymongo
import pandas as pd

MONGODB_DATABASE = 'examen'

try:
    client = pymongo.MongoClient('mongodb+srv://esfot:esfot@cluster0.n9mge.mongodb.net/examen?retryWrites=true&w=majority')
    client.server_info()
    print ('OK -- Connected to MongoDB Atlas at server %s' % ('cluster0'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB Atlas connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB Atlas: %s' % error)

db = client.examen
col = db.couchamongoatlas
    
my_cursor = col.find()

aux=[]
for item in my_cursor:
    aux.append(item)
    
pd.DataFrame([aux]).to_csv('examendatos.csv', index=False)