from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, SignInForm,  PasswordForm, ChangeForm, DeleteForm
from .models import Password
from .authmenu import renderauth, mergeDict
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .token import account_activation_token

# Create your views here.
def home(request):
    context = {
        'signinform': SignInForm(),
        'signupform': SignUpForm(),
        'passwordform': PasswordForm(),
        'changeform': ChangeForm(),
        'deleteform': DeleteForm(),
    }
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
            newuser = form.saveButDontActivate()
            form.sendActivationEmail(newuser)
            context = {"mainmessage":'Please confirm your email address'}
            return renderauth(request, "msg.html", context)
        else: 
            context = {"mainmessage":'One or more errors occurred', 'form': form}
            return renderauth(request, "msg.html", context) 
    return redirect("home")

def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            olduser = form.authenticateUser(request)
            if olduser is not None:
                form.sendNotification(olduser)
                login(request, olduser)
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

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        context = {"mainmessage":'Thank you for your email confirmation'}
        return renderauth(request, "msg.html", context)
    else:
        context = {"mainmessage":'Activation link is invalid!'}
        return renderauth(request, "msg.html", context)