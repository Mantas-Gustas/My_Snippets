from django.urls import path
from .views import *


urlpatterns = [
path('registration/', regform, name='registration-form'),
]
