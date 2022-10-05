import azure.cognitiveservices.speech as speechsdk

def translate_from_speech(language):
    speech_translation_config = speechsdk.translation.SpeechTranslationConfig(subscription="ac1b8fe3034344a787dc45b06243f51b", region="eastasia")
    speech_translation_config.speech_recognition_language=language

    target_languages = ['zh-Hant', 'en', 'es', 'fr', 'de', 'ja']

    for lan in target_languages:
        speech_translation_config.add_target_language(lan)

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    translation_recognizer = speechsdk.translation.TranslationRecognizer(translation_config=speech_translation_config, audio_config=audio_config)

    print("Speak into your microphone.")
    translation_recognition_result = translation_recognizer.recognize_once_async().get()

    if translation_recognition_result.reason == speechsdk.ResultReason.TranslatedSpeech:
        translate_result = {}
        for lan in target_languages:
            translate_result[lan] = translation_recognition_result.translations[lan]
            # print("Translated into '{}':{}".format(lan, translation_recognition_result.translations[lan]))
        return translate_result
    elif translation_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        for lan in target_languages:
            translate_result[lan] = "No speech could be recognized"
        print("No speech could be recognized: {}".format(translation_recognition_result.no_match_details))
        return translate_result
    elif translation_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = translation_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

# print(translate_from_speach("en-US"))