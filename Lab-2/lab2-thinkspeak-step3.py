import requests
import threading
import json

def read_data_thingspeak():
    URL='https://api.thingspeak.com/channels/1152483/feeds.json?api_key='
    KEY='RZGQ9FXZIQX5LZUP'
    HEADER='&results=3'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    feild_1=get_data['feeds']

    temp=[]
    for x in feild_1:
        temp.append(x['field1'])
    
    print ('The last 3 RPI CPU temperatures readings collected on Thinkspeak are:')
    print (temp)

if __name__ == '__main__':
    read_data_thingspeak()