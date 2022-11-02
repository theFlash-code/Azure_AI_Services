import azure.cognitiveservices.speech as speechsdk

SR_SUB_KEY='ac1b8fe3034344a787dc45b06243f51b'
TR_SUB_KEY='01ce4919dcd540fc8832a824102af1c4'
REGION='eastasia'
def recognize_from_microphone(language):
    speech_config = speechsdk.SpeechConfig(subscription=SR_SUB_KEY, region=REGION)
    print(speech_config.subscription_key)
    speech_config.speech_recognition_language=language

    # audio_input = speechsdk.audio.AudioConfig(use_default_microphone=True)
    audio_input = speechsdk.AudioConfig(filename="Wav_868kb.wav")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print("Speak into your microphone.")
    print("idk")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return format(speech_recognition_result.text)
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

recognize_from_microphone("en-US")