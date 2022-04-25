from django.db import models


class User_Profile(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length = 200)
    technologies = models.CharField(max_length=500)
    email = models.EmailField(default = None)
    display_picture = models.FileField()
    def __str__(self):
        return self.fname
    

#  display_picture is a File Field. It should have been an image field. We use a file field to store files on the server. It will create a File object which has many built-in attributes and methods. When a user uploads a file in the file field, we are storing file object in database and store file in MEDIA_ROOT. A file object is mainly to associate a file with an object or profile.