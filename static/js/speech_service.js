var phraseDiv;
var startRecognizeOnceAsyncButton;

// subscription key and region for speech services.
var subscriptionKey = "ac1b8fe3034344a787dc45b06243f51b",
  serviceRegion = "eastasia";
var SpeechSDK;
var recognizer;

document.addEventListener("DOMContentLoaded", function () {
  startRecognizeOnceAsyncButton = document.getElementById(
    "startRecognizeOnceAsyncButton"
  );
  //   subscriptionKey = document.getElementById("subscriptionKey");
  //   serviceRegion = document.getElementById("serviceRegion");
  subscriptionKey = "ac1b8fe3034344a787dc45b06243f51b";
  serviceRegion = "eastasia";
  phraseDiv = document.getElementById("phraseDiv");

  startRecognizeOnceAsyncButton.addEventListener("click", function () {
    startRecognizeOnceAsyncButton.disabled = true;
    phraseDiv.innerHTML = "";

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

    speechConfig.speechRecognitionLanguage = "en-US";
    var audioConfig = SpeechSDK.AudioConfig.fromDefaultMicrophoneInput();
    recognizer = new SpeechSDK.SpeechRecognizer(speechConfig, audioConfig);

    recognizer.recognizeOnceAsync(
      function (result) {
        startRecognizeOnceAsyncButton.disabled = false;
        phraseDiv.innerHTML += result.text;
        window.console.log(result);

        recognizer.close();
        recognizer = undefined;
      },
      function (err) {
        startRecognizeOnceAsyncButton.disabled = false;
        phraseDiv.innerHTML += err;
        window.console.log(err);

        recognizer.close();
        recognizer = undefined;
      }
    );
  });

  if (!!window.SpeechSDK) {
    SpeechSDK = window.SpeechSDK;
    startRecognizeOnceAsyncButton.disabled = false;

    document.getElementById("content").style.display = "block";
    document.getElementById("warning").style.display = "none";
  }
});
