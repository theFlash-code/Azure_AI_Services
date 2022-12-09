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

def brand_detection(url, language):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': CV_SUB_KEY,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'visualFeatures': 'Brands',
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

        # print(data)
        img = Image.open(requests.get(url, stream=True).raw)
        img_drw = ImageDraw.Draw(img)
        
        brands = data['brands']
        for brand in brands:
            rect = brand['rectangle']
            t = rect['y']
            l = rect['x']
            w = rect['w']
            h = rect['h']
            img_drw.rectangle([(l, t), (l+w, t+h)], outline ="red", width=7)

        return {"data":data, "img":img}

    except Exception as e:
        print(e)
        # print("[Errno {0}] {1}".format(e.errno, e.strerror))

# test()
print(brand_detection('https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/living-room-ideas-white-palette-1639423211.jpg', "en"))