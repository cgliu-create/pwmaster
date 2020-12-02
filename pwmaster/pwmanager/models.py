from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Password(models.Model):
    name = models.CharField(max_length=100)
    websitelink = models.URLField(max_length=100)
    pword = models.CharField(max_length=100)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_password',
    )

class PasswordGenerator(models.Model):
    letters = models.BooleanField()
    punctuation = models.BooleanField()
    digits = models.BooleanField()
    size = models.IntegerField()