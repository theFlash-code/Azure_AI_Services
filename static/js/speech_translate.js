// status fields and start button in UI
var resultsDivs;
var btn_translate;
var subscriptionKey = "ac1b8fe3034344a787dc45b06243f51b",
  serviceRegion = "eastasia";
// subscription key and region for speech services.
var languageTargetOptions;
var SpeechSDK;
var recognizer;

document.addEventListener("DOMContentLoaded", function () {
  btn_translate = document.getElementById("btn_translate");
  lang_slct = document.getElementById("lang_slct");
  languageTargetOptions = ["zh-Hant", "en", "es", "fr", "de", "ja"];
  resultsDivs = [
    document.getElementById("output_zh"),
    document.getElementById("output_en"),
    document.getElementById("output_es"),
    document.getElementById("output_fr"),
    document.getElementById("output_de"),
    document.getElementById("output_ja"),
  ];

  btn_translate.addEventListener("click", function () {
    btn_translate.disabled = true;
    resultsDivs.forEach(function (elem) {
      elem.value = "";
    });

    if (subscriptionKey === "" || subscriptionKey === "subscription") {
      alert(
        "Please enter your Microsoft Cognitive Services Speech subscription key!"
      );
      btn_translate.disabled = false;
      return;
    }
    var speechConfig = SpeechSDK.SpeechTranslationConfig.fromSubscription(
      subscriptionKey,
      serviceRegion
    );
    console.log(lang_slct.value);
    speechConfig.speechRecognitionLanguage = lang_slct.value;
    let languageKeys = {};
    languageTargetOptions.forEach(function (langElem, index) {
      let language = langElem;
      languageKeys[language] = resultsDivs[index];
      speechConfig.addTargetLanguage(language);
    });

    var audioConfig = SpeechSDK.AudioConfig.fromDefaultMicrophoneInput();
    recognizer = new SpeechSDK.TranslationRecognizer(speechConfig, audioConfig);

    recognizer.recognizeOnceAsync(
      function (result) {
        btn_translate.disabled = false;
        if (result.reason === SpeechSDK.ResultReason.TranslatedSpeech) {
          for (var key in languageKeys) {
            let translation = result.translations.get(key);
            window.console.log(key + ": " + translation);
            languageKeys[key].value += translation;
          }
        }

        recognizer.close();
        recognizer = undefined;
      },
      function (err) {
        btn_translate.disabled = false;
        resultsDiv[0].innerHTML += err;
        window.console.log(err);

        recognizer.close();
        recognizer = undefined;
      }
    );
  });

  if (!!window.SpeechSDK) {
    SpeechSDK = window.SpeechSDK;
    btn_translate.disabled = false;

    // document.getElementById("content").style.display = "block";
    // document.getElementById("warning").style.display = "none";
  }
});
