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
            member = MemberInfo.object.get(id=loginInfo['id'].value(),pw=loginInfo['pw'].value()+"1")
            request.session['auth_user_id'] = loginInfo['id'].value()
            request.session['power'] = member.classification
            print("dasdsa")
            return redirect("/")
        except ObjectDoesNotExist:
            loginInfo = LoginForm()
            context = {
                'loginInfo' : loginInfo,
                'alert' : True
            }
    else:
        loginInfo = LoginForm()
        context = {'loginInfo' : loginInfo,'alert' : False}
        
    return render(request, 'member/login.html',context)


# 회원가입
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
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
                member.save()
                return redirect(resolve_url('login'))
            else: #검증실패 시
                return render(request,'member/signup.html',{'signupInfo':form,'error':True})
    else:
        memberInfo = SignupForm()
        return render(request, 'member/signup.html',{'signupInfo':memberInfo})



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
    return redirect("/post/all")