from django.shortcuts import render, redirect, resolve_url
from .models import Post
from .forms import AddPostForm
# Create your views here.

def addPostView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            post = Post(title = form.data['title'], content = form.data['content'], user_id = request.session['_auth_user_id'])
            post.save()
            return render(request, 'test/test.html')#이거 바꿔야 함

        else :   
            form = AddPostForm()     
            return render(request, 'post/addPostView.html', {'form': form, 'error' : True})
    return render(request, 'post/addPostView.html')