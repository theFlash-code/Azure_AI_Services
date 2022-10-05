from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("speech_services/", views.speech_services, name="speech_services"),
    path("speech_translate/", views.speech_translate, name="speech_translate"),
    path("image_description/", views.image_description, name="image_description"),
    path("face_detection/", views.face_detection, name="face_detection"),
    path("area_of_interest/", views.area_of_interest, name="area_of_interest"),
    path("read_text/", views.read_text, name="read_text"),
    path("test/", views.test, name="test"),
]