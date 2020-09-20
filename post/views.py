from django.shortcuts import render, redirect, resolve_url
from .models import Post
from .forms import AddPostForm

# 잘 되게 해주세요
import os, sys
import sys
sys.path.append('../member/')
sys.path.append('../FirstLine/')
from member import views as MemberView
from FirstLine import init_analysis_model as SentimentAnalysisModel
import html2text
# Create your viewinit_analysis_model here.

def addPostView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        memberInfo = MemberView.get_memberInfo_model(request.session['auth_user_id'])
        if form.is_valid():
            sentiment_analyszer = SentimentAnalysisModel.SentimentAnalyszer.get_instance()
            content = html2text.html2text(form.data['content'])
            prob_n, prob_p, prob_dp, temperature = sentiment_analyszer.get_analysis_result(content)
            post = Post(title = form.data['title'], content = content, user_id = memberInfo, prob_p=prob_p,prob_dp=prob_dp,prob_n=prob_n,temperature=temperature)
            post.save()
            return render(request, 'alert_and_redirect.html', {'message' : "성공적으로 등록되었습니다", 'url' : "/"})
        else :   
            form = AddPostForm()     
            return render(request, 'alert_and_redirect.html', {'message' : "등록에 실패했습니다, 다시 등록해주세요", 'url' : "/post/add"})
    return render(request, 'post/addPostView.html')

def read_all(request):
    posts = Post.objects.all()
    posts = replace_enter(posts)
    return render(request, 'post/read_hot.html', {'posts' : posts})

def read_hot(request):
    posts = Post.objects.filter(temperature__gte = 38.0)
    posts = replace_enter(posts)
    return render(request, 'post/read_hot.html', {'posts' : posts})

def read_warm(request):
    posts = Post.objects.filter(temperature__range = (32.0 , 38.0))
    posts = replace_enter(posts)
    return render(request, 'post/read_hot.html', {'posts' : posts})

def read_cold(request):
    posts = Post.objects.filter(temperature__range = (1.0 , 32.0))
    posts = replace_enter(posts)
    return render(request, 'post/read_hot.html', {'posts' : posts})

def replace_enter(posts):
    for post in posts:
        
        post.content = post.content.split("\n")
        print(post.content)
        if isinstance(post.content, list):
            try:
                post.content.remove('')
            except Exception as ex:
                continue
    return posts
    