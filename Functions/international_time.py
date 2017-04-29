__author__ = 'Harsh'
import training
import config
import requests
import json
def t(query,flag):
    if(int(flag)!=1):
        continent=raw_input("Can you guess the Continent ?")
        query=continent+"/"+query
    #print(query)
    r=requests.get(config.time_api+query)
    #print(r)
    p=json.loads(r.text)
    #print(p['status'])
    if(p['status']=="FAILED"):
        print("umm there is some mistake...")
    #print(p['zoneName'],p['formatted'])
    else:
        print("Current time is %s in %s"%(p['formatted'],p['zoneName']))
        if(int(flag)!=1):
            i=raw_input("You got the answar ?")
            if(i=='yes'or i=="yeah"):
                training.save_time_entity(query)
            else:
                print("Nevermind, I am not that intelligent anyways")

