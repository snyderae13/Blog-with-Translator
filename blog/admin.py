from django.contrib import admin
from .models import Post

# this class allows for us to see in the admin interface when the post was created and who the author was along with the title of the post
# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date_created', 'author')

# Register your models here.
admin.site.register(Post, PostAdmin)