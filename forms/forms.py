from django import forms
from django.core import validators
from django.forms import TextInput, EmailInput


#DataFlair #Form
class SignUp(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'style': 'width: 300px;'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last name', 'style': 'width: 300px;'}))
    #first_name = forms.CharField(initial = 'First Name', )
    #last_name = forms.CharField(required = False)
    email = forms.EmailField(help_text = 'write your email', required = False)
    Address = forms.CharField(required = False, )
    Technology = forms.CharField(initial = 'Django', disabled = True)
    age = forms.IntegerField(required = False, )
    password = forms.CharField(widget = forms.PasswordInput, validators = [validators.MinLengthValidator(6)])
    re_password = forms.CharField(widget = forms.PasswordInput, required = False)
        
    # #DataFlair #Custom_Validator
    # def check_size(value):
    #     if len(value) < 6:
    #         raise forms.ValidationError("the Password is too short")
    
"""
Here in line 1, we imported a form class from Django. Then we created class SignUp. It is a sub-class of form class. Just like models, we defined different fields. It is almost similar to models class.

Required:
It takes value true or false. By default, it is true and makes necessary to fill the field. You can declare it false to change that.

Initial:
It provides the fields an initial value like textboxes come filled with some generic text. That is the initial argument.

Help-text:
If you want to display some instructions regarding that field, we use help-text. This attribute will display the string you pass in it.

Disabled:
Many times, we don’t want the user to change certain fields. In that case, we use the disabled parameter. It takes in true or false python Boolean. It will make the field static, i.e. the user cannot modified it .

Widget:
There are certain fields which can imitate different kinds of input. Like we have to use CharField for all text-related inputs including passwords. We can use widget attribute with Django’s built-in widgets like we used PasswordInput widget.

Validators:
This attribute will come in handy when we are using validations on data. There are built-in validators and we can also make custom ones.

Label:
This need not be defined if you want your field name to be displayed as the same as form. The label takes in a string and will display in front of the corresponding form field.

There are more attributes, but these are common to most of the fields.
"""