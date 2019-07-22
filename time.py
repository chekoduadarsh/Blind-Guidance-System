import requests
import io
import os
from base64 import b64encode
from os import makedirs
from os.path import join, basename
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

tat=strftime("%Y-%m-%d %H:%M:%S", gmtime())
tell('time is ')
tell(tat)
print(tat)
