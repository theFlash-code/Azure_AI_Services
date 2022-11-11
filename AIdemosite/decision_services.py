import requests, json  
CMD_SUB_KEY = "f24e093fcb564de394c2c2f80e6a4cb4"
REGION = "eastasia"

def content_moderator(text):
    key = CMD_SUB_KEY
    endpoint = "https://"+REGION+".api.cognitive.microsoft.com/"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = REGION

    path = 'contentmoderator/moderate/v1.0/ProcessText/Screen'
    constructed_url = endpoint + path

    params = {
        'autocorrect' : True,
        'PII' : True,
        'classify' : True,
        # 'language' : 'eng'
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Content-type': 'text/plain',
    }

    # You can pass more than one object in body.
    body = text

    request = requests.post(constructed_url, params=params, headers=headers, data=body)

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    response = request.json()
    return response

# print(content_moderator("Is this a crap email abcdef@abcd.com, phone: 6657789887, IP: 255.255.255.255, 1 Microsoft Way, Redmond, WA 98052"))
