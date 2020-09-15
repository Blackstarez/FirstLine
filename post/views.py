from django.shortcuts import render, redirect, resolve_url
from .models import Post
from .forms import AddPostForm

# 잘 되게 해주세요
import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname("../sementic_analysis"))))
from .views import sentimenticAnalysis

import sys
sys.path.append('../member/')
from member import views as MemberView
# Create your views here.

def addPostView(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        memberInfo = MemberView.get_memberInfo_model(request.session['auth_user_id'])
        if form.is_valid():
            post = Post(title = form.data['title'], content = form.data['content'], user_id = memberInfo)

            if sentimenticAnalysis(post): # 감성분석 성공이든 실패든 등록하게 되는 함수입니다.
                print('등록성공')
            else: print('등록실패')
            return render(request, 'alert_and_redirect.html', {'message' : "성공적으로 등록되었습니다", 'url' : "/"})
        else :   
            form = AddPostForm()     
            return render(request, 'alert_and_redirect.html', {'message' : "등록에 실패했습니다, 다시 등록해주세요", 'url' : "/post/add"})
    return render(request, 'post/addPostView.html')

def read_all(request):
    posts = Post.object.all()
    return render(request, 'post/read_all.html', {'posts' : posts})
