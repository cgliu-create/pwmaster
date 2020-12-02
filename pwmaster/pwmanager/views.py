from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, PasswordForm, PasswordGeneratorForm
from .models import Password, Manager
from .authmenu import renderauth, mergeDict
import string
import random

# Create your views here.
def home(request):
    context = {
        'signupform': SignUpForm(),
        'passwordform': PasswordForm(),
        'generatorform': PasswordGeneratorForm(),
    }
    if request.user.is_authenticated:
        xuser = request.user
        passwords = Password.objects.filter(user=User(id=xuser.id)
        pwmanager = Manager.objects.get(user=User(id=xuser.id)).pword
        authcontext = {
            'user': xuser,
            'passwords': passwords,
            'pwmanager': pwmanager,
        }
        temp = mergeDict(context, authcontext)
        context = temp
    return renderauth(request, "home.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            newuser = form.saveUser()
            manager = Manager.objects.create(user=User(id=newuser.id))
            manager.pword = ""
            manager.save()
    return redirect("home")

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect("home")

def createpassword(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            user = request.user 
            form.savePassword(user)
    return redirect("home")

def updatepassword(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            xuser = request.user 
            xname = self.cleaned_data['name']
            xpwword = self.cleaned_data['pword']
            passwords = Password.objects.filter(user=xuser.id)
            passwords = passwords.filter(name=xname)
            passwords = passwords.filter(pwword=xpwword)
            passwords.first().delete()
        form = PasswordForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            user = request.user 
            form.savePassword(user)
    return redirect("home")

def deletepassword(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            xuser = request.user 
            xname = self.cleaned_data['name']
            xpwword = self.cleaned_data['pword']
            passwords = Password.objects.filter(user=User(id=xuser.id)
            passwords = passwords.filter(name=xname)
            passwords = passwords.filter(pwword=xpwword)
            passwords.first().delete()
    return redirect("home")

def generatepassword(request):
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            xuser = request.user 
            password = form.newPassword()
            manager = Manager.objects.get(user=User(id=xuser.id))
            manager.pword = password
            manager.save()
    return redirect("home")



