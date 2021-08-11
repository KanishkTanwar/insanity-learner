from django.urls import path
from home.views import (index, backend, frontend,
                        quiz, insanity)

app_name = "home"

urlpatterns = [
    path('', index, name="index"),
    path('backend/', backend, name="backend"),
    path('frontend/', frontend, name="frontend"),
    path('insanity/', insanity, name="insanity"),
    path('quiz/', quiz, name="quiz"),
]