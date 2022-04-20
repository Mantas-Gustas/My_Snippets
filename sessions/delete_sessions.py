
#  Main URLs
path('delete/', include('student.urls')),
    

#  APP URLs
path('delete/', views.delete_session, name='delete-sess'),


def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>dataflair<br>Session Data cleared</h1>")


"""To delete a session or any particular key of that session, we can use del.

    del request.session['key_name']
"""