__author__ = 'Harsh'
import training
import config
import requests
import json
def w(query,flag):

    r=requests.get(config.weather_api+query+"%2C%20ak%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys")
    p=json.loads(r.text)
    temp_f=((((int(p['query']['results']['channel']['item']['forecast'][0][u'high'])-32)*5))/9)
    print("Weather at "+query+" is %s Degrees C"%(temp_f))
    if(int(flag)!=1):
        training.save_weather_entity(query)
    input()