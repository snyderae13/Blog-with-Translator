from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# a class for the blog post that will be a model class 
# https://docs.djangoproject.com/en/4.0/ref/models/instances/#django.db.models.Model

# a reference for the field types https://docs.djangoproject.com/en/4.0/ref/models/fields/



class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    #auto now add will add a date and time once the user clicks save
    slug = models.SlugField(max_length=100, unique=True)
    # this is to make sure that each post has a unique url /name
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # this sets the many to one relationship. and cascade will allow once a user is delete that their posts are deleted as well. 


    #__str__ is going to give us on the admin interface side an easier way to identify what the title of the post we create : https://docs.djangoproject.com/en/1.11/ref/models/instances/#str

    def __str__(self):
        return self.title
    