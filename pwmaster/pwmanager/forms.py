from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.forms import ModelForm
from .models import Password, PasswordGenerator
import string
import random
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .token import account_activation_token
from datetime import datetime

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=260, required=True)
    
    def saveButDontActivate(self):
        user = self.save(commit=False)
        user.is_active = False
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = user.email
        user.save()
        return  user  # for activation
    
    def sendActivationEmail(self, user):
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': settings.SITE_URL,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = self.cleaned_data.get('email')
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

class SignInForm(forms.Form):
    username = forms.CharField(max_length=100, required=True) 
    password = forms.CharField(max_length=100, required=True)

    def authenticateUser(self, request):
        xusername = self.cleaned_data['username']
        xpassword = self.cleaned_data['password']
        xuser = authenticate(request, username=xusername, password=xpassword)
        return xuser

    def sendNotification(self, user):
        mail_subject = 'Did you just log in to pwmanager?'
        now = datetime.now()
        dt_string = now.strftime("%m/%d/%Y %H:%M")
        message = render_to_string('notify_email.html', {
            'user': user,
            'date': dt_string,
        })
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send() 

class PasswordForm(ModelForm):
    name = forms.CharField(label='Username:', max_length=100)

    def savePassword(self, xuser):
        password = self.save(commit=False)
        password.name = self.cleaned_data['name']
        password.websitelink = self.cleaned_data['websitelink']
        password.pword = self.cleaned_data['pword']
        password.user = xuser
        password.save()

    class Meta:
        model = Password
        fields = ('name', 'website', 'websitelink', 'pword', )

class DeleteForm(forms.Form):
    oldname = forms.CharField(label='Old Username:', max_length=100, required=False)
    oldwebsite = forms.CharField(label='Old Website:', max_length=100, required=False)
    oldpword = forms.CharField(label='Old Pword:', max_length=100, required=False)

    def deletePassword(self, xuser):
        oldname = self.cleaned_data['oldname']
        oldwebsite = self.cleaned_data['oldwebsite'] 
        oldpword = self.cleaned_data['oldpword'] 
        passwords = Password.objects.filter(user=User(id=xuser.id))
        if oldname:
            passwords = passwords.filter(name=oldname)
        if oldwebsite:
            passwords = passwords.filter(website=oldwebsite)
        if oldpword:
            passwords = passwords.filter(pword=oldpword)
        old = passwords.first()
        old.delete()

class ChangeForm(ModelForm):
    oldname = forms.CharField(label='Old Username:', max_length=100, required=False)
    oldwebsite = forms.CharField(label='Old Website:', max_length=100, required=False)
    oldpword = forms.CharField(label='Old Pword:', max_length=100, required=False)
    name = forms.CharField(label='Username:', max_length=100, required=False)
    website = forms.CharField(label='Website:', max_length=100, required=False)
    websitelink = forms.URLField(label='Websitelink:', max_length=100, required=False)
    pword = forms.CharField(label='Pword:', max_length=100, required=False)
    
    def changePassword(self, xuser, old):
        if old:
            password = self.save(commit=False)
            if self.cleaned_data['name']:
               password.name = self.cleaned_data['name']
            else: 
                password.name = old.name
            if self.cleaned_data['website']:
                password.website = self.cleaned_data['website']
            else: 
                password.website = old.website
            if self.cleaned_data['websitelink']:
                password.websitelink = self.cleaned_data['websitelink']
            else: 
                password.websitelink = old.websitelink
            if self.cleaned_data['pword']:
                password.pword = self.cleaned_data['pword']
            else: 
                password.pword = old.pword
            password.user = xuser
            password.save()

    class Meta:
        model = Password
        fields = ('name', 'websitelink', 'pword', )

class PasswordGeneratorForm(ModelForm):

    def newPassword(self):
        letters = self.cleaned_data['letters'] 
        punctuation = self.cleaned_data['punctuation'] 
        digits = self.cleaned_data['digits'] 
        size = self.cleaned_data['size'] 
        password = ""
        if letters or punctuation or digits:
            characters = ""
            if letters:
                characters += string.ascii_letters
            if punctuation:
                characters += string.punctuation
            if digits:
                characters += string.digits
            for x in range(size):
                char = random.choice(characters)
                password = password + char
        return password

    class Meta:
        model = PasswordGenerator
        fields = ('letters', 'punctuation', 'digits', 'size') 
