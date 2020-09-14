from django.urls import path
from . import views

urlpatterns = [
    path('add', views.addPostView, name='addPostView' ),
    path('all', views.read_all, name='read_all' ),
]