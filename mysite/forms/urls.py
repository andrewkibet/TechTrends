from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name="signin"),
    path('home', views.home, name="home"),
    path('signup', views.signup, name="signup"),
    path('signout', views.signout, name="signout"),
    path('apply', views.apply, name="apply"),
    path('sup', views.sup, name="sup"),
    path('lapp', views.lapp, name="lapp"),
    path('assess', views.assess, name="assess"),
    path('test', views.test, name="test"),
]
