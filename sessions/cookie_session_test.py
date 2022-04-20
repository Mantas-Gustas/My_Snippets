from django.views.decorators.cache import cache_page

#  Main URLs
    path('testcookie/', include('student.urls')),
    path('deletecookie/', include('student.urls')),


#  APP URLs
    path('testcookie/', views.cookie_session, name='test-cookie'),
    path('deletecookie/', views.cookie_delete, name='delete-cookie'),

#  Checking Cookies on Browser
def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response