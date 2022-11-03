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
        return render(response, "AIdemosite/speech_services.html", {"s2t":"Click the button to use the speech to text service", "t2s":"Enter the text here", "translate_input":"Enter the text you want to translate"})

def speech_translate(response):

    if response.method == 'POST':
        from .speech_services import translate_from_speech
        language = response.POST.get('language-speach')
        translate_result = translate_from_speech(language)
        
        return render(response, "AIdemosite/speech_translate.html", {'zh':translate_result['zh-Hant'], 'en':translate_result['en'], 'es':translate_result['es'], 'fr':translate_result['fr'], 'de':translate_result['de'], 'ja':translate_result['ja']})
    else:
        return render(response, "AIdemosite/speech_translate.html", {})

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

def test(response):
    
    return render(response, "AIdemosite/test.html", {})
    
def api_instruction(response):
    if response.method == 'GET':
        # print(response)
        language = response.GET.get('language')
        print(language)
        return render(response, "AIdemosite/api_instructions.html", {"language":language})
    
    return render(response, "AIdemosite/api_instructions.html", {})