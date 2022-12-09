########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
from os import read
from PIL import Image, ImageDraw, ImageFont
import requests
import json
import environ
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential

# from AIdemosite.test import KVUri

# CV_SUB_KEY = '4b2c2c4a99cc4703973a809e965c3518'
# REGION = 'eastasia'

KVUri = "https://aidemosite-keyvault.vault.azure.net"
credential = DefaultAzureCredential()
client = SecretClient(vault_url=KVUri, credential=credential)

CV_SUB_KEY = client.get_secret("CV-SUB-KEY").value
REGION = client.get_secret("REGION").value

def image_description(url, visualFeatures):
    
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': CV_SUB_KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'visualFeatures': visualFeatures,
        'language': 'en',
        'model-version': 'latest',
    })

    try:
        conn = http.client.HTTPSConnection(REGION+'.api.cognitive.microsoft.com')
        # url = "https://th.bing.com/th/id/R.c3149655a1a145f0349a199e6bbe479e?rik=BEAyEveQSv47hg&pid=ImgRaw&r=0"
        conn.request("POST", "/vision/v3.2/analyze?%s" % params, ('{"url":"%s"}' % url), headers)
        response = conn.getresponse()
        data = response.read()
        
        data_json = data.decode('utf8')
        data = json.loads(data_json)
        conn.close()

        img = Image.open(requests.get(url, stream=True).raw)
        # img_drw = ImageDraw.Draw(img)  
        # face = data['faces']
        # for pos in face:
        #     rect = pos['faceRectangle']
        #     t = rect['top']
        #     l = rect['left']
        #     w = rect['width']
        #     h = rect['height']
        #     img_drw.rectangle([(l, t), (l+w, t+h)], outline ="red", width=7)

        return {"data":data, "img":img}

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
####################################

def face_detection(url, visualFeatures):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': CV_SUB_KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'visualFeatures': visualFeatures,
        'language': 'en',
        'model-version': 'latest',
    })

    try:
        conn = http.client.HTTPSConnection(REGION+'.api.cognitive.microsoft.com')
        # url = "https://th.bing.com/th/id/R.c3149655a1a145f0349a199e6bbe479e?rik=BEAyEveQSv47hg&pid=ImgRaw&r=0"
        conn.request("POST", "/vision/v3.2/analyze?%s" % params, ('{"url":"%s"}' % url), headers)
        response = conn.getresponse()
        data = response.read()
        
        data_json = data.decode('utf8')
        data = json.loads(data_json)
        conn.close()

        img = Image.open(requests.get(url, stream=True).raw)
        img_drw = ImageDraw.Draw(img)
        
        face = data['faces']
        for pos in face:
            rect = pos['faceRectangle']
            t = rect['top']
            l = rect['left']
            w = rect['width']
            h = rect['height']
            img_drw.rectangle([(l, t), (l+w, t+h)], outline ="red", width=7)
        
            img_drw.rectangle([(l, t-60), (l+150, t)], fill="white")
            font = ImageFont.truetype("AIdemosite/SansSerifFLF.otf", size=44)
            print("Age: "+str(pos['age']))
            img_drw.text((l, t-50), "Age: "+str(pos['age']), font=font, fill="black")
        # print("type of img: ", type(img))
        # img.show()
        return img


        


    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def area_of_interest(url):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': CV_SUB_KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'model-version': 'latest',
    })

    try:
        conn = http.client.HTTPSConnection(REGION+'.api.cognitive.microsoft.com')
        # url = "https://th.bing.com/th/id/R.c3149655a1a145f0349a199e6bbe479e?rik=BEAyEveQSv47hg&pid=ImgRaw&r=0"
        conn.request("POST", "/vision/v3.2/areaOfInterest?%s" % params, ('{"url":"%s"}' % url), headers)
        response = conn.getresponse()
        data = response.read()
        
        data_json = data.decode('utf8')
        data = json.loads(data_json)
        conn.close()

        print(data)
        img = Image.open(requests.get(url, stream=True).raw)
        img_drw = ImageDraw.Draw(img)
        
        area = data['areaOfInterest']
        
        t = area['y']
        l = area['x']
        w = area['w']
        h = area['h']
        img_drw.rectangle([(l, t), (l+w, t+h)], outline ="red", width=7)
        
        # img.show()
        
        return img


        


    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def read_text(url, language):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': CV_SUB_KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'language': language,
        'detectOrientation': 'true',
        'model-version': 'latest',
    })

    try:
        conn = http.client.HTTPSConnection(REGION+'.api.cognitive.microsoft.com')
        # url = "https://th.bing.com/th/id/R.c3149655a1a145f0349a199e6bbe479e?rik=BEAyEveQSv47hg&pid=ImgRaw&r=0"
        conn.request("POST", "/vision/v3.2/ocr?%s" % params, ('{"url":"%s"}' % url), headers)
        response = conn.getresponse()
        data = response.read()
        
        data_json = data.decode('utf8')
        data = json.loads(data_json)
        conn.close()
        print(data)

        language = data['language']
        lines = data['regions'][0]['lines']

        img = Image.open(requests.get(url, stream=True).raw)
        img_drw = ImageDraw.Draw(img)
        
        sentences = []
        for line in lines:
            bound = line['boundingBox']
            bound_cord = []
            sentence = ""
            for cord in bound.split(','):
                bound_cord.append(int(cord))
            for word in line['words']:
                # print(word)
                sentence += word['text']+" "
            print(sentence)
            print(bound_cord)
            img_drw.rectangle([(bound_cord[0]-10, bound_cord[1]-10), (bound_cord[0]+bound_cord[2]+10, bound_cord[1]+bound_cord[3]+10)], outline ="red", width=3)
            
            sentences.append(sentence)
            # font = ImageFont.truetype("SansSerifFLF.otf", size=20)
            # img_drw.text((bound_cord[0], bound_cord[1]-35), sentence, font=font, fill="black")
        print(sentences)
        return {"img":img, "sentences":sentences, "language":language}

        

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def obj_detection(url, language):
    
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': CV_SUB_KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'visualFeatures': 'Objects',
        'language': language,
        'model-version': 'latest',
    })

    try:
        conn = http.client.HTTPSConnection(REGION+'.api.cognitive.microsoft.com')
        # url = "https://th.bing.com/th/id/R.c3149655a1a145f0349a199e6bbe479e?rik=BEAyEveQSv47hg&pid=ImgRaw&r=0"
        conn.request("POST", "/vision/v3.2/analyze?%s" % params, ('{"url":"%s"}' % url), headers)
        response = conn.getresponse()
        data = response.read()
        
        data_json = data.decode('utf8')
        data = json.loads(data_json)
        conn.close()

        
        img = Image.open(requests.get(url, stream=True).raw)
        img_drw = ImageDraw.Draw(img)
        
        objects = data['objects']
        for obj in objects:
            rect = obj['rectangle']
            t = rect['y']
            l = rect['x']
            w = rect['w']
            h = rect['h']
            img_drw.rectangle([(l, t), (l+w, t+h)], outline ="red", width=7)
            obj_name = obj['object']
            img_drw.rectangle([(l, t-60), (l+(23*len(obj_name)), t)], fill="white")
            font = ImageFont.truetype("arial.ttf", size=44)
            img_drw.text((l, t-50), str(obj_name), font=font, fill="black")
        # img.show()
        return {"data":data, "img":img}

    except Exception as e:
        print(e)
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def test():
    data = {
        "description": {
            "captions": [
                {
                    "confidence": 0.586622953414917,
                    "text": "a group of men playing football"
                }
            ],
            "tags": [
                "person",
                "grass",
                "soccer",
                "field",
                "playing",
                "outdoor",
                "player",
                "game",
                "match",
                "female"
            ]
        },
        "faces": [
            {
                "age": 27,
                "faceRectangle": {
                    "height": 122,
                    "left": 508,
                    "top": 200,
                    "width": 122
                },
                "gender": "Male"
            },
            {
                "age": 29,
                "faceRectangle": {
                    "height": 110,
                    "left": 1530,
                    "top": 202,
                    "width": 110
                },
                "gender": "Male"
            },
            {
                "age": 24,
                "faceRectangle": {
                    "height": 102,
                    "left": 759,
                    "top": 224,
                    "width": 102
                },
                "gender": "Male"
            }
        ],
        "metadata": {
            "format": "Jpeg",
            "height": 1413,
            "width": 2120
        },
        "modelVersion": "2021-05-01",
        "requestId": "af4fd9af-5923-4d84-b9de-b8bcca566e5b"
    }

    url = "https://th.bing.com/th/id/R.c3149655a1a145f0349a199e6bbe479e?rik=BEAyEveQSv47hg&pid=ImgRaw&r=0"
    img = Image.open(requests.get(url, stream=True).raw)
    
    # create rectangle image
    img_drw = ImageDraw.Draw(img)  

    face = data['faces']
    for pos in face:

        rect = pos['faceRectangle']
        t = rect['top']
        l = rect['left']
        w = rect['width']
        h = rect['height']
        img_drw.rectangle([(l, t), (l+w, t+h)], outline ="red", width=7)
        img_drw.rectangle([(l, t-60), (l+150, t)], fill="white")
        font = ImageFont.truetype("AIdemosite/SansSerifFLF.otf", size=44)
        print("Age: "+str(pos['age']))
        img_drw.text((l, t-50), "Age: "+str(pos['age']), font=font, fill="black")

    # img.show()
    return img
