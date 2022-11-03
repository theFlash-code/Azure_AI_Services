var text_result;
var btn_s2t;

var subscriptionKey = "ac1b8fe3034344a787dc45b06243f51b",
  serviceRegion = "eastasia";
var SpeechSDK;
var recognizer;

document.addEventListener("DOMContentLoaded", function () {
  btn_s2t = document.getElementById("btn_s2t");
  text_result = document.getElementById("result");

  btn_s2t.addEventListener("click", function () {
    btn_s2t.disabled = true;
    text_result.innerHTML = "";

    if (subscriptionKey === "" || subscriptionKey === "subscription") {
      alert(
        "Please enter your Microsoft Cognitive Services Speech subscription key!"
      );
      return;
    }
    var speechConfig = SpeechSDK.SpeechConfig.fromSubscription(
      subscriptionKey,
      serviceRegion
    );
    var lang_slct = document.getElementById("lang_slct");
    speechConfig.speechRecognitionLanguage = lang_slct.value;
    var audioConfig = SpeechSDK.AudioConfig.fromDefaultMicrophoneInput();
    recognizer = new SpeechSDK.SpeechRecognizer(speechConfig, audioConfig);

    recognizer.recognizeOnceAsync(
      function (result) {
        btn_s2t.disabled = false;
        text_result.innerHTML += result.text;
        window.console.log(result);

        recognizer.close();
        recognizer = undefined;
      },
      function (err) {
        btn_s2t.disabled = false;
        text_result.innerHTML += err;
        window.console.log(err);

        recognizer.close();
        recognizer = undefined;
      }
    );
  });

  if (!!window.SpeechSDK) {
    SpeechSDK = window.SpeechSDK;
    btn_s2t.disabled = false;
  }
});
