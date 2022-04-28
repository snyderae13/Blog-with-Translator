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

#class HomeView(generic.TemplateView):
   #template_name = 'index.html'

# this is to create a class for a view for the Posts that I want to display as a list on the homepage.
# I found that ListView is the best option for this beacuase it is a page representing a list of objects. 

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-date_created')
    #queryset is used to search through my posts model and order them by date created in descending order when they are populated into the index html : https://docs.djangoproject.com/en/4.0/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    template_name = 'index.html'