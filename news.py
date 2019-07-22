import requests
import io
import os
from sys import argv
import json
import requests
from pygame import mixer          # Load the required library
from gtts import gTTS
from timeit import default_timer as timer
from time import gmtime, strftime
from playsound import playsound

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def tell(a):
    language = 'en'
    myobj = gTTS(text=a, lang=language, slow=False)
    myobj.save("temp.mp3")
    playsound('temp.mp3')


def  weather():

    #Weather based disease prediction
    # api-endpoint
    URL="http://api.openweathermap.org/data/2.5/weather?lat=12.9716&lon=77.5946&appid=5afbaa57cd77fbb92036676d548636d3"


    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    # extracting data in json format
    data = json.loads(r.text)

    tm =data['main']['temp']
    hum =data['main']['humidity']

    name=data['name']
    tmp=tm-273
    print(tmp)
    print(hum)
    print(name)
    tmp = str(round(tmp, 2))
    tell('todays weather is')
    tell(str(name))
    
    tell('temperature is')
    tell(str(tmp))
    tell('digree celsius')
    tell('humidity is')
    tell(str(hum))

tell('Reading news')
tat=strftime("%Y-%m-%d %H:%M:%S", gmtime())
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=a4391775167245c0b5fc089876b0e27c')               #API link note: i have removed my personal apiKey


tell('time is ')
tell(tat)


weather()



response = requests.get(url)
data=response.json()
name1=data['articles'][0]['source']['name']
title1=data['articles'][0]['title']
pub1=data['articles'][0]['publishedAt']
name2=data['articles'][1]['source']['name']
title2=data['articles'][1]['title']
pub2=data['articles'][1]['publishedAt']
name3=data['articles'][2]['source']['name']
title3=data['articles'][2]['title']
pub3=data['articles'][1]['publishedAt']
name4=data['articles'][3]['source']['name']
title4=data['articles'][3]['title']
pub4=data['articles'][1]['publishedAt']


tell('main news and headlines')
print(name1)
tell(name1)
print (title1)
tell(title1)
print(pub1)
#tell(pub1)
print(name2)
tell(name2)
print (title2)
tell(title2)
print(pub2)
#tell(pub2)
print(name4)
tell(name4)
print (title4)
tell(title4)
print(pub4)
#tell(pub4)
print(name3)
tell(name3)
print (title3)
tell(title3)
print(pub3)
#tell(pub3)
