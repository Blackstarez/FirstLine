from django.shortcuts import render, redirect, resolve_url
from .models import Post
from .forms import AddPostForm

# 잘 되게 해주세요
#import os, sys
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(sementic_analysis))))
#from .views import sentimenticAnalysis

# Create your views here.

def addPostView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = Post(title = form.data['title'], content = form.data['content'], user_id = request.session['_auth_user_id'])
            post.save()
            #sentimenticAnalysis('글번호 넘겨주세요')
            return render(request, 'test/test.html')#이거 바꿔야 함

        else :   
            form = AddPostForm()     
            return render(request, 'post/addPostView.html', {'form': form, 'error' : True})
    return render(request, 'post/addPostView.html')

def read_all(request):
    posts = Post.object.all()
    return render(request, 'post/read_all.html', {'posts' : posts})
