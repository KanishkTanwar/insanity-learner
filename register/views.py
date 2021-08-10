from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages

# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        form = CreateUserForm()
        context = {'form': form}
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('home:index')

        return render(request, 'register/signin.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('home:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home:index')
            else:
                messages.warning(request, 'Username OR password is incorrect')

        return render(request, 'register/signin.html')


def signout(request):
    logout(request)
    return redirect('home:index')