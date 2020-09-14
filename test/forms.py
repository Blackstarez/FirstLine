from django import forms
from .models import Test
default = {
    'required': '이 항목은 필수 항목입니다.',
    'invalid': '올바르지 않은 값입니다.',
    'unique': '이미 등록된 값입니다. 이 항목은 중복된 값으로 등록될 수 없습니다.'
}

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control mb-3'})
            field.error_messages = default