from django.urls.resolvers import URLPattern
from accounts.api import LoginAPI, UserAPI, RegisterAPI
from django.urls import path

urlpatterns = [

    path("login/", LoginAPI.as_view()),
    path("register/", RegisterAPI.as_view()),
    path("user/", UserAPI.as_view()),
]