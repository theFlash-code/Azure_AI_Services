from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("speech_services/", views.speech_services, name="speech_services"),
    path("speech_translate/", views.speech_translate, name="speech_translate"),
    path("speech_to_text/", views.speech_to_text, name="speech_to_text"),
    path("text_to_speech/", views.text_to_speech, name="text_to_speech"),
    path("language_sentiment/", views.language_sentiment, name="language_sentiment"),
    path("language_keyPhrases/", views.language_keyPhrases, name="language_keyPhrases"),
    path("image_description/", views.image_description, name="image_description"),
    path("face_detection/", views.face_detection, name="face_detection"),
    path("area_of_interest/", views.area_of_interest, name="area_of_interest"),
    path("read_text/", views.read_text, name="read_text"),
    path("content_moderator/", views.content_moderator, name="content_moderator"),
    path("test/", views.test, name="test"),
    path("api_instructions/", views.api_instruction, name="api_instructions"),
    path("ms_ignite/", views.ms_ignite, name="ms_ignite")
]