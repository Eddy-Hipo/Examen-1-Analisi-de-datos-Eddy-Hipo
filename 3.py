import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import pymongo
import json
from facebook_scraper import get_posts

aux=[]

for post in get_posts('82061850555', pages=10):  #ID de una página
    text = post['text']; 
    image = post['image'];
    video=  post['video']; 
    likes = post['likes'];
    share =  post['shares'];
    comments = post['comments'];
    link =  post['link'];
    data = {
    'text' : text, 'image' : image,
    'video': video, 'likes': likes,
    'share': share, 'comments': comments,
    'link': link}
    aux.append(data) 

URI_CONNECTION = 'mongodb://localhost:27017'
MONGODB_DATABASE = 'examen'

try:
    client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=100000, maxPoolSize=10)
    client.server_info()
    print ('OK -- Connected to MongoDB at server %s' % ('localhost'))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print ('Error with mongoDB connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print ('Could not connect to MongoDB: %s' % error)
    
for x in range(0,len(aux)):
    data=aux[x]
    try:
        destination = 'facebook'
        collection = client[MONGODB_DATABASE][destination]
        collection.insert_one(data)
        print ("Data saved at %s collection in %s database: %s" % (destination, MONGODB_DATABASE, data))
    except Exception as error:
        print ("Error saving data: %s" % str(error))