from django.shortcuts import render
from . import forms


#DataFlair #Form #View Functions
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "The Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html': html, 'form': form})


"""
In above view function, we have declared forms the same as we declared models. We created a new instance of form class. Then we checked by which method we are receiving our form, whether, it’s POST method or any other method.

This condition is important. It will check whether the user is requesting the form for the first time or has filled data before. When a user demands form for the first time, we receive a GET request but when a user submits data in form, it will happen through POST request. Thus, we will send the right response.
"""