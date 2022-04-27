from pyexpat import model
from django.shortcuts import render
from .models import Post

# Create your views here.
# view docs : https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/


class BlogView:
    model = Post
    template_name = 'blog.html'