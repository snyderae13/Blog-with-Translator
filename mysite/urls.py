"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

#in here we declare all of the url patterns we create in the blog folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('about/', include('blog.urls')),
]

# I ran into an early problem with using curly brackets over square for my url patterns in this file and my blogs urls file. It should always be set to square brackets otherwise the /admin path will not work
# https://stackoverflow.com/questions/42952940/typeerror-at-admin-set-object-is-not-reversible

