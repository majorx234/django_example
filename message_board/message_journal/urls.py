from django.urls import path
#from . import admin
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.message_overview, name='overview'),
    path('createPost', views.create_post, name='create_post')
    ]
