import io
import os
import os
from base64 import b64encode
from os import makedirs
from os.path import join, basename
from sys import argv
import json
import requests
from google.cloud.vision import types
from google.cloud.bigquery.client import Client
import io
import os
from pygame import mixer          # Load the required library
from gtts import gTTS
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from playsound import playsound

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def tell(a):
    language = 'en'
    myobj = gTTS(text=a, lang=language, slow=False)
    myobj.save("temp.mp3")

    playsound('temp.mp3')




def detect_logos(path):
    """Detects logos in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('Logos:')

    for logo in logos:
        tell('logo is')
        print(logo.description)
        tell(logo.description)



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Blind-Guidance-44e49a875d12.json' #give path to your Service account keys .json file
bq_client = Client()
path='logo.png'    					  #give path to your image
detect_logos(path)
