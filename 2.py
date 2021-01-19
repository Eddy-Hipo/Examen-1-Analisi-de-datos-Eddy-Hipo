import pandas as pd
from bs4 import BeautifulSoup
import requests
import time
import pymongo
import json

def find_2nd(string, substring):
    return string.find(substring, string.find(substring) + 1)
def find_1st(string, substring):
    return string.find(substring, string.find(substring))

response = requests.get("https://news.blizzard.com/es-es")
soup = BeautifulSoup(response.content, "lxml")

Title = []
Description = []
Time = []
Game = []

post_title=soup.find_all("a", class_="ArticleLink ArticleLink")
post_description=soup.find_all("div", class_="h6")
post_time=soup.find_all("time", class_="ArticleListItem-footerTimestamp")
post_game=soup.find_all("small", class_="flush-top ArticleListItem-labelInner")

for element in post_title:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Title.append(limpio.strip())
    
for element in post_description:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Description.append(limpio.strip())
    
for element in post_time:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Time.append(limpio.strip())
    
for element in post_game:
    element=str(element)
    limpio=str(element[find_1st(element, '>')+1:find_2nd(element, '<')])
    Game.append(limpio.strip())

aux=[]
for x in range(0,len(Title)):
    data={'title':Title[x],'description':Description[x],'time':Time[x],'game':Game[x]}
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
        destination = 'juegos'
        collection = client[MONGODB_DATABASE][destination]
        collection.insert_one(data)
        print ("Data saved at %s collection in %s database: %s" % (destination, MONGODB_DATABASE, data))
    except Exception as error:
        print ("Error saving data: %s" % str(error))