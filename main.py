__author__ = 'Harsh'
import weather
import config

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer,WordNetLemmatizer
ps=PorterStemmer()
lemmatizer=WordNetLemmatizer()

def check(a,intent):
    if(intent=="weather"):
        print(a)
        list_to_return=[]
        file=open('weather_data.txt','r')
        for i in a:
            for j in file:
                #print(i)
                #print(j)
                if((i+'\n')==j):

                    list_to_return.append(i)
                    list_to_return.append('1')
                    print("matched and returned successfully")
                    return list_to_return

            file.seek(0)

                
            
def intent(a):
    for i in a:
        for j in config.intents:
            #print(str(i).lower())
            if(str(i).lower()==j):
                return i
def entity(a,intent):
    checked=check(a,intent)
    try:
        #print(type(checked))
        #print(checked[-1])
        if(int(checked[-1])==1):
            return checked                  #IF we get in last data
    except TypeError :
        tagged=nltk.pos_tag(a)
        list_intents=[]
        named_entity=nltk.ne_chunk(tagged,binary=True) #name entity recognition
        #print(named_entity)
        for i in named_entity:
            if(hasattr(i,'label') and i.label()):     #checking if label exists
                if(i.label()=="NE"):                  #if its a named entity
                    list_intents.append(i[0][0])
                    list_intents.append('0')
                    print("Dint match and returned")
                    return list_intents



text=raw_input("input":)
words=word_tokenize(text)           #tokenizing
stop_words=set(stopwords.words("english"))
a=[]
for w in words:
    if(w not in stop_words):    #Stopwords removal
        stemmed=ps.stem(w)                          #stemming
        a.append(lemmatizer.lemmatize(stemmed))    #lemmatizing

final_intent=intent(a) # We got the intent
#print(final_intent)
final_entity=entity(words,final_intent)   #we got entity   , and we got everything
#print(final_entity)


if(final_intent=='weather'):
    weather.w(final_entity[0],final_entity[-1])















