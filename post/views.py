from django.shortcuts import render
from .models import Post
# Create your views here.

def addPostView(request):
    return render(request, 'post/addPostView.html')

def read_all(request):
    posts = Post.object.all()
    return render(request, 'post/read_all.html', {'posts' : posts})