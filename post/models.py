from django.db import models
# Create your models here. #DataFlair 

class Post(models.Model):
    post_heading = models.CharField(max_length = 200)
    post_text = models.TextField()
    post_author = models.CharField(max_length = 100, default = 'anonymous')
    
    
class Like(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE)


# Here, Post and Like are two models. We are using the Foreign Key Field. It is used to define many-to-one relationships between models. The post variable in Like model will contain the primary key of the post that we added. Thus, we can then refer to that post’s data. We are not using it in this example though.