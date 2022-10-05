
import http.client, urllib.request, urllib.parse, urllib.error, base64
from PIL import Image, ImageDraw, ImageFont
import requests
import json

# data = {
#         'language': 'en',
#         'textAngle': 0.0,
#         'orientation': 'Up',
#         'regions': [
#             {
#                 'boundingBox': '491,269,217,93', 
#                 'lines': 
#                 [
#                     {
#                         'boundingBox': '491,269,217,21', 
#                         'words': 
#                         [
#                             {'boundingBox': '491,270,71,20', 'text': 'YOUR'},
#                             {'boundingBox': '571,269,60,20', 'text': 'TEXT'},
#                             {'boundingBox': '642,269,66,21', 'text': 'HERE'}
#                         ]
#                     }, 
#                     {
#                         'boundingBox': '534,342,132,20', 
#                         'words': 
#                         [
#                             {'boundingBox': '534,343,53,19', 'text': 'AND'},
#                             {'boundingBox': '600,342,66,20', 'text': 'HERE'}
#                         ]
#                     }
#                 ]
#             }], 
#         'modelVersion': '2021-04-01'
#     }


# language = data['language']
# orientation = data['orientation']
# lines = data['regions'][0]['lines']

# img = Image.open(requests.get('https://rlv.zcache.com/custom_your_text_image_background_color_bumper_sticker-r9a7314b88be545a4886346db9bb7cf95_v9wht_8byvr_630.jpg?view_padding=[285%2C0%2C285%2C0]', stream=True).raw)
# img_drw = ImageDraw.Draw(img)

# for line in lines:
#     bound = line['boundingBox']
#     bound_cord = []
#     sentence = ""
#     for cord in bound.split(','):
#         bound_cord.append(int(cord))
#     for word in line['words']:
#         # print(word)
#         sentence += word['text']+" "
#     print(sentence)
#     print(bound_cord)
#     img_drw.rectangle([(bound_cord[0]-10, bound_cord[1]-10), (bound_cord[0]+bound_cord[2]+10, bound_cord[1]+bound_cord[3]+10)], outline ="red", width=3)
    
#     # img_drw.rectangle([(bound_cord[0], bound_cord[1]-60), (bound_cord[0]+150, bound_cord[1])], fill="white")
#     font = ImageFont.truetype("SansSerifFLF.otf", size=20)
#     img_drw.text((bound_cord[0], bound_cord[1]-35), sentence, font=font, fill="black")

# img.show()

# lan = "zh-Hans (ChineseSimplified)zh-Hant (ChineseTraditional)cs (Czech)da (Danish)nl (Dutch)en (English)fi (Finnish)fr (French)de (German)el (Greek)hu (Hungarian)it (Italian)ja (Japanese)ko (Korean)nb (Norwegian)pl (Polish)pt (Portuguese,ru (Russian)es (Spanish)sv (Swedish)tr (Turkish)ar (Arabic)ro (Romanian)sr-Cyrl (SerbianCyrillic)sr-Latn (SerbianLatin)sk (Slovak)"
# lan = lan.replace(' (', '":"')
# lan = lan.replace(')', ",")
# print(lan)
# lans = lan.split(',')
# print(lans)
import environ
import os
env = environ.Env()
env.read_env(env.str('ENV_PATH', '../demosite/.env'))
CV_SUB_KEY = env('CV_SUB_KEY')
print(env('REGION'))
# print(env('CV_SUB_KEY'))
# print(os.environ.get('CV_SUB_KEY'))