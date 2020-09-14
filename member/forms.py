from django import forms
from .models import MemberInfo

default = {
    'required': '이 항목은 필수 항목입니다.',
    'invalid': '올바르지 않은 값입니다.',
    'unique': '이미 등록된 값입니다. 이 항목은 중복된 값으로 등록될 수 없습니다.'
}

# 로그인 폼
class LoginForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['id','pw']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            field.error_messages = default

# 회원가입 폼
class SignupForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['id', 'pw','name','age','sex','email','phoneNumber','address','offerInfoAgree']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            field.error_messages = default

# 회원정보 조회 폼(사용자 개인)
class MemberInfoReadOnlyForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['id', 'pw','name','age','sex','email','phoneNumber','address','creationDate','offerInfoAgreeDay']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs.update()
            field.error_messages = default