from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signup"),
    path("signout", views.signout, name="signout"), 
    path("create", views.createpassword, name="create"), 
    path("update", views.updatepassword, name="update"), 
    path("delete", views.deletepassword, name="delete"), 
]
