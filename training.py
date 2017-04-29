__author__ = 'Harsh'


def save_weather_entity(entity):
    f=open('weather_data.txt','a')
    entity=entity+'\n'
    f.write(entity)
    print("File saved")
