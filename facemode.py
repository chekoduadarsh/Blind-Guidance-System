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
    '''
    mixer.init()
    mixer.music.load('/home/adarsh/Desktop/MEWA/visionocr/temp.mp3')
    mixer.music.play()
    setup_player('/home/adarsh/Desktop/MEWA/visionocr/temp.mp3')
    '''
    playsound('temp.mp3')



def detect_faces(path):
    """Detects faces in an image."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    print('Faces:')

    for face in faces:
        anger=format(likelihood_name[face.anger_likelihood])
        joy=format(likelihood_name[face.joy_likelihood])
        surp=format(likelihood_name[face.surprise_likelihood])
        tell('his emotion is')
        if ((anger =='POSSIBLE') or (anger =='LIKELY') or (anger =='VERY_LIKELY')):
            tell('angry')
            print('angry')
        if ((joy =='POSSIBLE') or (joy =='LIKELY') or (joy =='VERY_LIKELY')):
            tell('happy')
            print('happy')
        if ((surp =='POSSIBLE') or (surp =='LIKELY') or (surp =='VERY_LIKELY')):
            tell('surprised')
            print('surprised')
        if ((joy == 'UNKNOWN') or (surp == 'UNKNOWN')  or (anger == 'UNKNOWN') ):
            tell('unidentifiable')
            print('unidentifiable')
            
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in face.bounding_poly.vertices])

        print('face bounds: {}'.format(','.join(vertices)))



os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'Blind-Guidance-44e49a875d12.json' #give path to your Service account keys .json file
bq_client = Client()
path='face2.jpg'    					  #give path to your image
detect_faces(path)

