########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64
from os import read
from PIL import Image, ImageDraw, ImageFont
import requests
import json

# from AIdemosite.test import KVUri


# KVUri = "https://aidemosite-keyvault.vault.azure.net"
# credential = DefaultAzureCredential()
# client = SecretClient(vault_url=KVUri, credential=credential)

CV_SUB_KEY = "4b2c2c4a99cc4703973a809e965c3518"
REGION = 'eastasia'


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
        img.show()
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
        font = ImageFont.truetype("arial.ttf", size=44)
        print("Age: "+str(pos['age']))
        img_drw.text((l, t-50), "Age: "+str(pos['age']), font=font, fill="black")

    img.show()
    return img

# test()
print(obj_detection('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/living-room-ideas-white-palette-1639423211.jpg', "en"))