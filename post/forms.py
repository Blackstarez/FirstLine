from django import forms
from .models import Post

class AddPostForm(forms.Form):
    title = forms.CharField(        
        error_messages={
            'required': '글의 제목을 입력해주세요'
        },
        max_length=25, label="글제목")

    content = forms.CharField(
        error_messages={
            'required': '본문을 입력해주세요'
        },
        max_length=1000, label="본문")