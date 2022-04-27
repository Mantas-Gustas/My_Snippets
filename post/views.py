from django.shortcuts import render
from .models import Post, Like
from django.http import HttpResponse


# Create your views here.
#DataFlair #AJAX_tutorial
def index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', { 'posts': posts })


def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        likedpost = Post.objects.get(id = post_id )
        m = Like( post=likedpost )
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")
    
    
# We created two view functions. The first one is to render all the posts and the second one is for the like function.
# The like function exists to handle the AJAX request from like button. As you can see, it is similar to the function that we use in forms.

# The like function will first check for the request. If it is the GET method, then it will read the data. The data is the id of the post we liked. Then, we create a Like class object and save its id equal to data. Then, we store the object in our database.

# At last, we are returning an HttpResponse. This response will do nothing in our code as we are not printing the same. We could have just passed a script. These can be utilized according to one’s use case.