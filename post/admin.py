from django.contrib import admin
from .models import *


# Register your models here.
#DataFlair #AJAX
admin.site.register(Post)
admin.site.register(Like)


# the above imports models inside admin page