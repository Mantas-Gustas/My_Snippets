# basic_api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('basic/', views.API_objects.as_view()),
    path('basic/<int:pk>/', views.API_objects_details.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


# In this code, we have created a urls.py file. There are some new terms here though. The new import is from rest_framework.urlpatterns. The format_suffix_patterns method will be used to generalize our urls. It will make the urls to work with URIs like

# http://basic/4 and http://basic/4.json

# Both of these urls can be handled by our web app. Then we imported the views from the basic_api app. After that, we simply defined the urls.

# The new part is the view function we have written. This is what you call a view from a Class-Based Views in Django. In the view functions, we write the name of the class. The class name is always accompanied by the as_view() method. This is true for all CBVs out there and is not limited to DRF.

# That’s it. After that the format_sufix_patterns() is used on urlpatterns.