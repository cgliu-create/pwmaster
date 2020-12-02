from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Password, PasswordGenerator

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=260, required=True)
    
    def saveUser(self):
        user = self.save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.username = user.email
        return user

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )

class PasswordForm(ModelForm):

    def savePassword(self, user):
        password = self.save(commit=False)
        password.name = self.cleaned_data['name']
        password.websitelink = self.cleaned_data['websitelink']
        password.pword = self.cleaned_data['pword']
        password.user = user.id
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
