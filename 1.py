import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
###API ########################
ckey = "Uj23AID5byBYDgpMdzt3skkqP"
csecret = "WQnwXDZ9WEXEGwwVQDnxsinrPQdSSpEk74ln9C6Z3TOJzHAndC"
atoken = "596652588-r3IZ4SR354FkwuRnSgHM1aumXfoTgYfKQ4IA3mRR"
asecret = "yQpmFB0n9MgPPGmBN0mr7g5U6PdK4IMRGiC9jWhnSchC9"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://Eddy:elieddy2203z@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('examen')
except:
    db = server['examen']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-78.619545,-0.408764,-78.259892,-0.047208])  
twitterStream.filter(track=['videogames'])