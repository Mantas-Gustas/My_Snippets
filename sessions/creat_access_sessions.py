"""
Understanding the Code:

The code follows basic python, but the variables we are using have some complex python coding behind them.

When you request for access/ URL without running the create/ request, you redirect to the create/ automatically if you have no cookie generated previously.

Now, when the create/ URL is sent, the SessionsMiddleware runs and generates a unique SessionID which is stored locally on the browser as a cookie for the user.

This cookie is now sent to the server every time alongside with the request and sessions. The application does the work of matching the SessionID with one in the database. It also stores some values and variables which we have created in the create_session() view function.

The request object has a session attribute and when the server runs that code, the session middleware, and sessions application automatically works together.4

request.session[] act as a python dictionary data-structure, and therefore, you can store the values alongside with their keys having meaningful names.

In the access_session() function, we have used get() alongside request.session and passed the value of the key.

Thus, you can access the sessions easily.

Therre are many methods that associate with session argument of the HttpRequest object.

"""

#  Main URLs
    path('create/', include('student.urls')),
    path('access/', include('student.urls')),

#  APP URLs
    path('create/', views.create_session, name='create-sess'),
    path('access/', views.access_session, name='access-sess'),


def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>dataflair<br> the session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions of dataflair</h1><br>"
    if request.session.get('name'):
        response += "Name : {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password : {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')



#  settings

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    #DataFlair #Caching Middleware
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]