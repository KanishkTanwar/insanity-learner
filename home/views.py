from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "home/index.html")


def backend(request):
    return render(request, "home/backend.html")


def frontend(request):
    return render(request, "home/frontend.html")


def insanity(request):
    return render(request, "home/insanity.html")


def quiz(request):
    return render(request, "home/quiz.html")