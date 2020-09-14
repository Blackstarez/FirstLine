from django.shortcuts import render, redirect, resolve_url, get_object_or_404
from .models import MemberInfo
from .forms import *
from django.core.exceptions import ObjectDoesNotExist
import re
from django.contrib import messages
from datetime import datetime

# Create your views here.

# 로그인 - 세션에 사용자 id와 권한(관리자 여부)를 기록
def login(request):
    if request.method == 'POST':
        loginInfo = LoginForm(request.POST)
        try:
            member = MemberInfo.object.get(id=loginInfo['id'].value(),pw=loginInfo['pw'].value())
            request.session['auth_user_id'] = loginInfo['id'].value()
            request.session['power'] = member.classification
            return redirect("/")
        except ObjectDoesNotExist:
            return render(request, "alert_and_redirect.html", { 'message':"로그인에 실패했습니다", 'url' : "/"})
        
        
    


# 회원가입
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            print("dasdsa")
            if isValidSignUp(form):
                if form.data['offerInfoAgree'] == 1:
                    member = MemberInfo(id=form.data['id'],pw=form.data['pw'],name=form.data['name'],
                    age=form.data['age'],sex=form.data['sex'],email=form.data['email'],
                    phoneNumber=form.data['phoneNumber'],address=form.data['address'],offerInfoAgree=form.data['offerInfoAgree'],
                    offerInfoAgreeDay=datetime.today().strftime("%Y%m%d%H%M%S"),creationDate=datetime.today().strftime("%Y%m%d%H%M%S"))
                else:
                    member = MemberInfo(id=form.data['id'],pw=form.data['pw'],name=form.data['name'],
                    age=form.data['age'],sex=form.data['sex'],email=form.data['email'],
                    phoneNumber=form.data['phoneNumber'],address=form.data['address'],offerInfoAgree=form.data['offerInfoAgree'],
                    offerInfoAgreeDay='00000000000000',creationDate=datetime.today().strftime("%Y%m%d%H%M%S"))
                request.session['auth_user_id'] = member.id
                request.session['power'] = member.classification
                member.save()
            else:
                return render(request, "alert_and_redirect.html", { 'message':"회원가입에 실패했습니다. 입력정보를 확인해주세요", 'url' : "/"})
        else:
            return render(request, "alert_and_redirect.html", { 'message':"회원가입에 실패했습니다. 입력정보를 확인해주세요", 'url' : "/"})
    
    return render(request, "alert_and_redirect.html", { 'message':"축하드립니다 성공적으로 가입되었습니다", 'url' : "/"})



# 회원가입 정보 검증 (전화번호, 이메일) /ID,PW 등등은 추후 추가 예정
def isValidSignUp(memberInfo):
    phoneNum = re.compile('[0-9]{2,3}-[0-9]{3,4}-[0-9]{4,4}')
    email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if(phoneNum.match(memberInfo['phoneNumber'].value())):
        if(email.match(memberInfo['email'].value())):
            return True
        else: return False
    else: return False

def logout(request):
    del request.session['auth_user_id']
    del request.session['power']
    return redirect("/")