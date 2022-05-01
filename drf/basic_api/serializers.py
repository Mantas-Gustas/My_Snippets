from rest_framework import serializers
from .models import DRFPost


class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'
        
# Let’s understand what we just did. We created a new file serializers.py in our application. This file contains the code similar to modelforms code.

# We imported the serializer class from the rest_framework module. This is the DRF used in Django. They couldn’t use Django as it would conflict with the existing name itself. Then we imported the model we wanted serializer for.

# Then like model forms class, we created serializer class. This is called the model serializer class. The model serializer class will take the model attribute and field attribute.

# The model attribute will input the model for the serializer. The fields attribute takes a list containing the names of fields. These are the fields which will be passed as a json file. Now, we will also need views and urls to see how all this works.