from django.shortcuts import render, redirect, resolve_url
from .models import Post
from .forms import AddPostForm

# 잘 되게 해주세요
import os, sys
sys.path.append('../sentimentic_analysis/')
from sentimentic_analysis import views as SentimenticView

import sys
sys.path.append('../member/')
sys.path.append('../FirstLine/')
from member import views as MemberView
from FirstLine import init_analysis_model as SentimentAnalysisModel
# Create your viewinit_analysis_model here.

def addPostView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        memberInfo = MemberView.get_memberInfo_model(request.session['auth_user_id'])
        if form.is_valid():
<<<<<<< HEAD
            sentiment_analyszer = SentimentAnalysisModel.SentimentAnalyszer.get_instance()
            prob_n, prob_p, prob_dp, temperature = sentiment_analyszer.get_analysis_result(str(form.data['content']))
            post = Post(title = form.data['title'], content = form.data['content'], user_id = memberInfo, prob_p=prob_p,prob_dp=prob_dp,prob_n=prob_n,temperature=temperature)
            post.save()
=======
            post = Post(title = form.data['title'], content = form.data['content'], user_id = memberInfo)

            if SentimenticView.sentimenticAnalysis(post): # 감성분석 성공이든 실패든 등록하게 되는 함수입니다.
                print('등록성공')
            else: print('등록실패')
>>>>>>> 7c2286ac2c86279da5ae8777aa1dcbc70a49610d
            return render(request, 'alert_and_redirect.html', {'message' : "성공적으로 등록되었습니다", 'url' : "/"})
        else :   
            form = AddPostForm()     
            return render(request, 'alert_and_redirect.html', {'message' : "등록에 실패했습니다, 다시 등록해주세요", 'url' : "/post/add"})
    return render(request, 'post/addPostView.html')

def read_all(request):
    posts = Post.objects.all()
    return render(request, 'post/read_all.html', {'posts' : posts})

def read_hot(request):
    posts = Post.objects.filter(temperature_gte = 38.0)
    return render(request, 'post/read_hot.html', {'posts' : posts})
