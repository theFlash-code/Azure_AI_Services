import azure.cognitiveservices.speech as speechsdk
import requests, json  #, uuid
import environ

# env = environ.Env()
# env.read_env(env.str('ENV_PATH', 'demosite/.env'))

# SR_SUB_KEY = env('SR_SUB_KEY')
# TR_SUB_KEY = env('TR_SUB_KEY')
# REGION = env('REGION')s

SR_SUB_KEY='ac1b8fe3034344a787dc45b06243f51b'
TR_SUB_KEY='01ce4919dcd540fc8832a824102af1c4'
REGION='eastasia'

# def recognize_from_microphone(language):
#     speech_config = speechsdk.SpeechConfig(subscription=SR_SUB_KEY, region=REGION)
#     print(speech_config.subscription_key)
#     speech_config.speech_recognition_language=language

#     # audio_input = speechsdk.audio.AudioConfig(use_default_microphone=True)
#     audio_input = speechsdk.AudioConfig(filename="audiotest.wav")
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

#     print("Speak into your microphone.")
#     print("idk")
#     speech_recognition_result = speech_recognizer.recognize_once_async().get()

#     if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(speech_recognition_result.text))
#         return format(speech_recognition_result.text)
#     elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
#     elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = speech_recognition_result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")

# def read_txt_quickstart():
#     speech_config = speechsdk.SpeechConfig(subscription=SR_SUB_KEY, region=REGION)
#     audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#     # The language of the voice that speaks.
#     speech_config.speech_synthesis_voice_name='en-US-JennyNeural'

#     speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#     # Get text from the console and synthesize to the default speaker.
#     print("Enter some text that you want to speak >")
#     text = input()

#     speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

#     if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#         print("Speech synthesized for text [{}]".format(text))
#     elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = speech_synthesis_result.cancellation_details
#         print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             if cancellation_details.error_details:
#                 print("Error details: {}".format(cancellation_details.error_details))
#                 print("Did you set the speech resource key and region values?")

# def read_txt(txt, language):
#     speech_config = speechsdk.SpeechConfig(subscription=SR_SUB_KEY, region=REGION)
#     audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

#     # The language of the voice that speaks.
#     speech_config.speech_synthesis_voice_name=language
#     print(language)
#     speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

#     # Get text from the console and synthesize to the default speaker.
#     # print("Enter some text that you want to speak >")
#     # text = input()

#     speech_synthesis_result = speech_synthesizer.speak_text_async(txt).get()

#     if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
#         print("Speech synthesized for text [{}]".format(txt))
#     elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = speech_synthesis_result.cancellation_details
#         print("Speech synthesis canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             if cancellation_details.error_details:
#                 print("Error details: {}".format(cancellation_details.error_details))
#                 print("Did you set the speech resource key and region values?")

# def translate_from_speech(language):
#     speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription=SR_SUB_KEY, region=REGION)
#     speech_translation_config.speech_recognition_language=language

#     target_languages = ['zh-Hant', 'en', 'es', 'fr', 'de', 'ja']

#     for lan in target_languages:
#         speech_translation_config.add_target_language(lan)

#     audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
#     translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

#     print("Speak into your microphone.")
#     translation_recognition_result = translation_recognizer.recognize_once_async().get()

#     if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
#         translate_result = {}
#         for lan in target_languages:
#             translate_result[lan] = translation_recognition_result.translations[lan]
#             # print("Translated into '{}':{}".format(lan, translation_recognition_result.translations[lan]))
#         return translate_result
#     elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
#         for lan in target_languages:
#             translate_result[lan] = "No speech could be recognized"
#         print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
#         return translate_result
#     elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = translation_recognition_result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")

# def from_file(language):
#     speech_config = speechsdk.SpeechConfig(subscription=SR_SUB_KEY, region=REGION)
#     speech_config.speech_recognition_language=language

#     audio_config = speechsdk.audio.AudioConfig(filename="audiotest.wav")
#     speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

#     print("Speak into your microphone.")
#     print("idk")
#     speech_recognition_result = speech_recognizer.recognize_once_async().get()

#     if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
#         print("Recognized: {}".format(speech_recognition_result.text))
#         return format(speech_recognition_result.text)
#     elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
#         print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
#     elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
#         cancellation_details = speech_recognition_result.cancellation_details
#         print("Speech Recognition canceled: {}".format(cancellation_details.reason))
#         if cancellation_details.reason == speechsdk.CancellationReason.Error:
#             print("Error details: {}".format(cancellation_details.error_details))
#             print("Did you set the speech resource key and region values?")


def translate(text, translate_from, translate_to):
    # Add your key and endpoint
    key = TR_SUB_KEY
    endpoint = "https://api.cognitive.microsofttranslator.com"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
    location = REGION

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': translate_from,
        'to': [translate_to]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        # 'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)

    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))

    response = request.json()
    translation = response[0]['translations'][0]['text']
    return translation
