import allauth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout, authenticate, login

# Create your views here.


def index(request):
    template = loader.get_template('oneplace/index.html')
    if request.user.is_authenticated:
        context = {
            'loggedin': True,
        }
    else:
        context = {
            'loggedin': False,
        }

    return HttpResponse(template.render(context, request))


def chatapp(request, id):
    return HttpResponse("You're looking at illness %s." % id)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_cancelled(request):
    return redirect('/')

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)
    template = loader.get_template('oneplace/index.html')
    if user is not None:
        login(request, user)
        context = {
            'loggedin': True,
            'loginerror': False,
        }
    else:
        context = {
            'loggedin': False,
            'loginerror': True,
        }

    return redirect('/')
