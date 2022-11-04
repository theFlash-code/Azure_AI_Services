import requests, json  
LAN_SUB_KEY = "d90b6c7972c24b06bb9f9e19f09b567b"
REGION = "eastasia"
def sentiment_analyze(text, lan):
    key = LAN_SUB_KEY
    endpoint = "https://"+REGION+".api.cognitive.microsoft.com/"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = REGION

    path = 'text/analytics/v3.1/sentiment'
    constructed_url = endpoint + path

    params = {
        'showStats' : 'true',
        'opinionMining' : 'true',
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        # 'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        # 'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = json.dumps({
        "documents": [
            {
            "id": "1",
            "language": lan,
            "text": text,
            }
        ]
    })

    request = requests.post(constructed_url, params=params, headers=headers, data=body)

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    response = request.json()
    return response

# print(sentiment("Great atmosphere. Close to plenty of restaurants, hotels, and transit! Staff are friendly and helpful.", "en"))