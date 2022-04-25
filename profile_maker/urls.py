from django.urls import path
from .views import *
from myproject import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', create_profile, name = 'create-profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
    
#  Concentrate on the if section. We are using these settings only when the project is in debug mode. Then we have added these patterns to the urlpatterns variable. These patterns are referred when a media file is requested. These settings are important when serving the file uploaded by the user.

# Although, these are only used when you are developing a website. The server settings are different for servers.