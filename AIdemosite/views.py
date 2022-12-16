from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from PIL import Image
import io


# Create your views here.

code_to_language = {
    'zh-Hans':'ChineseSimplified',
    'zh-Hant':'ChineseTraditional',
    'cs':'Czech',
    'da':'Danish',
    'nl':'Dutch',
    'en':'English',
    'fi':'Finnish',
    'fr':'French',
    'de':'German',
    'el':'Greek',
    'hu':'Hungarian',
    'it':'Italian', 
    'ja':'Japanese',
    'ko':'Korean',
    'nb':'Norwegian',
    'pl':'Polish',
    'pt':'Portuguese',
    'ru':'Russian',
    'es':'Spanish',
    'sv':'Swedish',
    'tr':'Turkish',
    'ar':'Arabic',
    'ro':'Romanian',
    'sr-Cyrl':'SerbianCyrillic',
    'sr-Latn':'SerbianLatin',
    'sk':'Slovak'
}

def index(response):
    return render(response, "AIdemosite/home.html", {})

def speech_to_text(response):
    return render(response, "AIdemosite/speech_to_text.html", {})

def text_to_speech(response):
    return render(response, "AIdemosite/text_to_speech.html", {})

def speech_translate(response):

    if response.method == 'POST':
        from .speech_services import translate_from_speech
        language = response.POST.get('language-speach')
        translate_result = translate_from_speech(language)
        
        return render(response, "AIdemosite/speech_translate.html", {'zh':translate_result['zh-Hant'], 'en':translate_result['en'], 'es':translate_result['es'], 'fr':translate_result['fr'], 'de':translate_result['de'], 'ja':translate_result['ja']})
    else:
        return render(response, "AIdemosite/speech_translate.html", {})

def speech_services(response):
    if response.method == 'POST':
        # print(response.POST)
        # print('btn-t2s' in response.POST)
        print()
    if response.method == 'POST' and 'btn_s2t' in response.POST:
        # Speech-to-text
        from .speech_services import from_file, recognize_from_microphone
        language_s2t = response.POST.get('language-s2t')
        txt = recognize_from_microphone(language_s2t)
        
        return render(response, "AIdemosite/speech_services.html", {"s2t":txt, "t2s":"Enter the text here", "translate_input":txt})
    elif response.method == 'POST' and 'btn-translate' in response.POST:
        # Translation
        print(response.POST)
        s2t = response.POST.get('s2t')
        
        translate_from_txt = response.POST.get('translate_from_txt')
        translate_from_lan = response.POST.get('translate_from_lan')
        translate_to_lan = response.POST.get('translate_to_lan')

        from .speech_services import translate
        translate_result = translate(translate_from_txt, translate_from_lan, translate_to_lan)
        
        
        return render(response, "AIdemosite/speech_services.html", {"s2t":s2t, "translate_input":translate_from_txt,"t2s":translate_result, "translate_result":translate_result})

    elif response.method == 'POST' and 'btn_t2s' in response.POST:
        # Text-to-speech
        s2t = response.POST.get('s2t')
        translate_input = response.POST.get('translate_from_txt')
        translate_result = response.POST.get('translate_result')

        language_sound = response.POST.get('language-t2s')
        t2s = response.POST.get('input_t2s')
        from .speech_services import read_txt
        read_txt(t2s, language_sound)

        return render(response, "AIdemosite/speech_services.html", {"s2t":s2t, "t2s":t2s, "translate_input":translate_input, "translate_result":translate_result})
    else:
        return render(response, "AIdemosite/speech_services.html", {"s2t":"Click the button to use the speech to text service", "t2s":"Enter the text here"})

def language_sentiment(response):
    # print('btn-analyze' in response.POST)
    if response.method == 'POST' :
        from .language_services import sentiment_analyze
        text = response.POST.get('input_text')
        lan = response.POST.get('lang_slct')
        result = sentiment_analyze(text, lan)
        
        sentiment = result['documents'][0]['sentiment']
        confidence = result['documents'][0]['confidenceScores']
        sentences = result['documents'][0]['sentences']
        cnt = 0
        for sen in sentences:
            cnt += 1
            sen['cnt'] = cnt

        return render(response, "AIdemosite/language_sentiment.html", {"text":text, "sentiment":sentiment, "confidence":confidence, "sentences":sentences, "flag":True})

    return render(response, "AIdemosite/language_sentiment.html", {})

def language_keyPhrases(response):
    if response.method == 'POST' :
        from .language_services import keyPhrases_analyze
        text = response.POST.get('input_text')
        lan = response.POST.get('lang_slct')
        result = keyPhrases_analyze(text, lan)
        phrases = result['documents'][0]['keyPhrases']
        return render(response, "AIdemosite/language_keyPhrases.html", {"flag":True, "text":text, "phrases":phrases})

    return render(response, "AIdemosite/language_keyPhrases.html", {})

#Computer Vision
def image_description(response):
    
    if response.method == 'POST':
        from .computer_vision_analysis import image_description
        url = response.POST.get('img-url')
        data = image_description(url, "description,faces")
        # data = test()
        img = data['img']
        descriptions = data['data']['description']
        img.save("static/images/description_result.jpg")
        return render(response, "AIdemosite/image_description.html", {"descriptions":descriptions, "flag":True})

    return render(response, "AIdemosite/image_description.html", {"flag":False})
        
def face_detection(response):
    if response.method == 'POST':
        from .computer_vision_analysis import face_detection, test
        url = response.POST.get('img-url')
        print(" -----------------------------------------------test----------------------------------------------------- ")
        print(url)
        img = face_detection(url, 'faces')
        # img = test()
        print(type(img))
        img.save("static/images/face_detection_result.jpg")
        return render(response, "AIdemosite/face_detection.html", {"flag":True})

    return render(response, "AIdemosite/face_detection.html", {})

def area_of_interest(response):
    if response.method == 'POST':
        from .computer_vision_analysis import area_of_interest
        url = response.POST.get('img-url')
        img = area_of_interest(url)
        img.save("static/images/area_of_interest_result.jpg")
        return render(response, "AIdemosite/area_of_interest.html", {"flag":True})

    return render(response, "AIdemosite/area_of_interest.html", {})

def img_sumbnail(response): 
    if response.method == 'POST':
        from .computer_vision_analysis import img_sumbnail
        url = response.POST.get('img-url')
        w = response.POST.get('img-w')
        h = response.POST.get('img-h')
        img = img_sumbnail(url, w, h)
        img.save("static/images/img_sumbnail.jpg")
        return render(response, "AIdemosite/img_sumbnail.html", {"url":url, "flag":True})

    return render(response, "AIdemosite/img_sumbnail.html", {"flag":False})



def read_text(response):
    if response.method == 'POST':
        from .computer_vision_analysis import read_text
        url = response.POST.get('img-url')
        data = read_text(url, 'unk')
        img = data['img']
        sentences = data['sentences']
        img.save("static/images/read_text_result.jpg")
        return render(response, "AIdemosite/read_text.html", {"flag":True, "sentences":sentences, "language":code_to_language[data['language']]})

    return render(response, "AIdemosite/read_text.html", {})

def content_moderator(response):
    if response.method == 'POST' :
        from .decision_services import content_moderator
        text = response.POST.get('input_text')
        result = content_moderator(text)
        print(text)
        print(result)
        correct = result["AutoCorrectedText"]
        print(correct)
        return render(response, "AIdemosite/content_moderator.html", {"flag":True, "text":text, "result":result, "correct":correct})

    return render(response, "AIdemosite/content_moderator.html", {})

def obj_detection(response):
    if response.method == 'POST':
        from .computer_vision_analysis import obj_detection
        url = response.POST.get('img-url')
        language = 'en'
        r_data = obj_detection(url, language)
        data = r_data['data']['objects']
        img = r_data['img']
        img.save("static/images/obj_detection_result.jpg")
        return render(response, "AIdemosite/object_detection.html", {"flag":True, "data":data})

    return render(response, "AIdemosite/object_detection.html", {})

def brand_detection(response):
    if response.method == 'POST':
        from .computer_vision_analysis import brand_detection
        url = response.POST.get('img-url')
        language = 'en'
        r_data = brand_detection(url, language)
        data = r_data['data']['brands']
        img = r_data['img']
        img.save("static/images/brand_detection_result.jpg")
        return render(response, "AIdemosite/object_detection.html", {"flag":True, "data":data})

    return render(response, "AIdemosite/object_detection.html", {})

def img_categories(response):
    
    if response.method == 'POST':
        from .computer_vision_analysis import img_categories
        url = response.POST.get('img-url')
        data = img_categories(url, "en")
        return render(response, "AIdemosite/img_categories.html", {"data":data, "url":url, "flag":True})

    return render(response, "AIdemosite/img_categories.html", {"flag":False})

def img_color(response):
    
    if response.method == 'POST':
        from .computer_vision_analysis import img_color
        url = response.POST.get('img-url')
        data = img_color(url, "en")
        return render(response, "AIdemosite/img_color.html", {"data":data[0], "url":url, "flag":True})

    return render(response, "AIdemosite/img_color.html", {"flag":False})
   
def img_type(response):
    
    if response.method == 'POST':
        from .computer_vision_analysis import img_type
        url = response.POST.get('img-url')
        data = img_type(url, "en")
        return render(response, "AIdemosite/img_type.html", {"data":data, "url":url, "flag":True})

    return render(response, "AIdemosite/img_type.html", {"flag":False})



def test(response):
    
    return render(response, "AIdemosite/test.html", {})
    
def api_instruction(response):
    if response.method == 'GET':
        # print(response)
        language = response.GET.get('language')
        print(language)
        return render(response, "AIdemosite/api_instructions.html", {"language":language})
    
    return render(response, "AIdemosite/api_instructions.html", {})

def ms_ignite(response):
    if response.method == 'GET':
        language = response.GET.get('language')
        print(language)
        return render(response, "AIdemosite/ms_ignite.html", {"language":language})
    
    return render(response, "AIdemosite/ms_ignite.html", {})