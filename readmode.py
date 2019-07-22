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
    print('mp3 created')
    playsound('temp.mp3')



def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print(texts)
    print('Texts:')
    count=1
    for text in texts:
        a=("{}".format(text.description))
        if (count == 1 ):
            tell(a)
            print(a)
        count=count+1
    
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Blind-Guidance-44e49a875d12.json' #give path to your Service account keys .json file
bq_client = Client()
path='ocr3.png'
print('processing')                     #give path to your image
detect_text(path)

