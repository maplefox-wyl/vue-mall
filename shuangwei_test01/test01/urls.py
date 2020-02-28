from django.conf.urls import url

from . import views
from django.urls import path
urlpatterns = [
    path('user', views.user),
    path("test/",views.test),
    path("login",views.login),
]