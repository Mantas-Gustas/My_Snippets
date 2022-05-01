from django.shortcuts import render
from rest_framework import generics
from .models import DRFPost
from .serializers import DRFPostSerializer


class API_objects(generics.ListCreateAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
    
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFPost.objects.all()
    serializer_class = DRFPostSerializer
    
    
#     In the first 4 lines, we are importing all the important things we are going to need in view. We imported models, serializer class and generics class. The generics class will provide us with the web browsable API. The generics class is a special class in rest_framework.

# There are also generic views for Django itself. They are for a different purpose.

# You need to keep it in mind that this is an API. It’s not meant to be displayed to the user. It’s for programs or applications communication. The generics class will provide us with important classes. These classes make it easy to deal with RESTful requests and send JSON data.

# The first view class is Post_objects. This class extends the class generics.ListCreateAPIView class. It is clear from the name. This class will be used to provide a list of all model instances. These model instances will be converted to JavaScript objects and transmit to application.

# There are two fields in this class. The first is the Queryset attribute. This attribute will provide the model instances to be operated on. The view classes are written by DRF developers and we need not learn what’s it doing behind the scenes. The second attribute it asks for is serializer_class.

# The serializer class we just imported is entered there.

# This means that this is the serializer model to be used to create a JSON model. The view part will handle the calling of correct classes and queries. It will then respond with the JSON response to the client or other application.

# The second view class is also similar to the 1st. I discussed earlier; this view logics are not needed to be known. You should know what results we get. You do not need to reinvent the wheel or have an understanding of the whole framework. The second class will provide details of an individual object.

# There are more operations that can be performed on an individual object. Therefore, we are using class generics.RetrieveUpdateDestroyAPIView class. This class will provide Read, Update and Delete Functions on the model instance. Ok, now let’s set up the urls.

# Configuring URLs