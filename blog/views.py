from pyexpat import model
from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
# view docs : https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/


class BlogView(generic.DetailView):
    model = Post
    template_name = 'blog.html'

# this is to make sure that when the user goes to '', or the homepage that our views call on the index html template that we built, and we use a template view because we are just rendering a given template
# https://www.geeksforgeeks.org/templateview-class-based-generic-view-django/

class HomeView(generic.TemplateView):
    template_name = 'index.html'