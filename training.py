__author__ = 'Harsh'


def save_weather_entity(entity):
    f=open('weather_data.txt','a')
    entity=entity+'\n'
    f.write(entity)
    print("File saved")
def save_time_entity(entity):
    f=open('time_data.txt','a')
    entity=entity+'\n'
    f.write(entity)
    print("File saved")
