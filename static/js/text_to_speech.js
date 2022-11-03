var subscriptionKey = "ac1b8fe3034344a787dc45b06243f51b",
  serviceRegion = "eastasia";
var SpeechSDK;
var recognizer;

var inputDiv;
var btn_t2s;

// subscription key and region for speech services.
var subscriptionKey, serviceRegion;
var SpeechSDK;
var synthesizer;

document.addEventListener("DOMContentLoaded", function () {
  btn_t2s = document.getElementById("btn_t2s");
  console.log(btn_t2s);
  inputDiv = document.getElementById("inputDiv");

  btn_t2s.addEventListener("click", function () {
    btn_t2s.disabled = true;

    if (
      subscriptionKey.value === "" ||
      subscriptionKey.value === "subscription"
    ) {
      alert(
        "Please enter your Microsoft Cognitive Services Speech subscription key!"
      );
      btn_t2s.disabled = false;
      return;
    }
    var speechConfig = SpeechSDK.SpeechConfig.fromSubscription(
      subscriptionKey,
      serviceRegion
    );

    synthesizer = new SpeechSDK.SpeechSynthesizer(speechConfig);
    console.log(inputDiv);
    let inputText = inputDiv.value;
    synthesizer.speakTextAsync(
      inputText,
      function (result) {
        btn_t2s.disabled = false;
        if (
          result.reason === SpeechSDK.ResultReason.SynthesizingAudioCompleted
        ) {
          resultDiv.innerHTML +=
            "synthesis finished for [" + inputText + "].\n";
        } else if (result.reason === SpeechSDK.ResultReason.Canceled) {
          resultDiv.innerHTML +=
            "synthesis failed. Error detail: " + result.errorDetails + "\n";
        }
        window.console.log(result);
        synthesizer.close();
        synthesizer = undefined;
      },
      function (err) {
        btn_t2s.disabled = false;
        resultDiv.innerHTML += "Error: ";
        resultDiv.innerHTML += err;
        resultDiv.innerHTML += "\n";
        window.console.log(err);

        synthesizer.close();
        synthesizer = undefined;
      }
    );
  });

  if (!!window.SpeechSDK) {
    SpeechSDK = window.SpeechSDK;
    btn_t2s.disabled = false;

    // in case we have a function for getting an authorization token, call it.
    if (typeof RequestAuthorizationToken === "function") {
      RequestAuthorizationToken();
    }
  }
});
