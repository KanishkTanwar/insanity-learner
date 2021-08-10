from django.shortcuts import render

# Create your views here.


def signin(request):
    return render(request, 'register/signin.html')


def signout(request):
    return render(request, 'register/signin.html')