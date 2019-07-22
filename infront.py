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


def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')
    tell('i can see')
    for label in labels:
        print(label.description)
        tell(label.description)

tell('Detecting the scene') 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '' #give path to your Service account keys .json file
bq_client = Client()
path='view.jpg'    					  #give path to your image
detect_labels(path)
