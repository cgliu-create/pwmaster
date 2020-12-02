from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, PasswordForm, PasswordGeneratorForm, ChangeForm, DeleteForm
from .models import Password
from .authmenu import renderauth, mergeDict
from django.contrib.auth.models import User
import string
import random

# Create your views here.
def home(request):
    context = {
        'signupform': SignUpForm(),
        'passwordform': PasswordForm(),
        'changeform': ChangeForm(),
        'deleteform': DeleteForm(),
        'generatorform': PasswordGeneratorForm(),
    }
    if request.method == 'POST':
        form = PasswordGeneratorForm(request.POST)
        if form.is_valid():
            password = form.newPassword()
            pwcontext = {'generatedpw':password, }
            temp = mergeDict(context, pwcontext)
            context = temp

    if request.user.is_authenticated:
        xuser = request.user
        passwords = Password.objects.filter(user=User(id=xuser.id))
        authcontext = {
            'user': xuser,
            'passwords': passwords,
        }
        temp = mergeDict(context, authcontext)
        context = temp
    return renderauth(request, "home.html", context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            newuser = form.saveUser()
    return redirect("home")

def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        xuser = authenticate(request, username=username, password=password)
        if xuser is not None:
            login(request, xuser)
    return redirect("home")

def signout(request):
    logout(request)
    return redirect("home")

def createpassword(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            xuser = request.user 
            form.savePassword(xuser)
    return redirect("home")

def updatepassword(request):
    if request.method == 'POST':
        form = ChangeForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            xuser = request.user 
            oldname = request.POST['oldname']
            oldpword = request.POST['oldpword']
            passwords = Password.objects.filter(user=User(id=xuser.id))
            if oldname:
                passwords = passwords.filter(name=oldname)
            if oldpword:
                passwords = passwords.filter(pword=oldpword)
            old = passwords.first()
            form.changePassword(xuser, old)
            old.delete()
    return redirect("home")

def deletepassword(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            xuser = request.user 
            form.deletePassword(xuser)
    return redirect("home")
