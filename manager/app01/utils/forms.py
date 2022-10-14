"""
# @Time    : 2022/10/12 15:31
# @Author  : violet
# @explain : 
"""

from django import forms
from django.core.validators import RegexValidator
from django.core.validators import ValidationError
from .. import models


class UserModelForm(forms.ModelForm):
    name = forms.CharField(label='用户名', min_length=3, max_length=16)

    # password = forms.CharField(label='密码', validators='正则表达式')

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class PrettyUpdateModelForm(forms.ModelForm):
    mobile = forms.CharField(label='手机号', disabled=True)

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}


class PrettyModelForm(forms.ModelForm):
    # 验证方式一
    mobile = forms.CharField(
        label='号码',
        validators=[RegexValidator('^1[3-9][0-9]{9}$', '手机格式错误')]
    )

    class Meta:
        model = models.PrettyNum
        # fields = '__all__'
        fields = ['mobile', 'price', 'level', 'status']
        # exclude = []  排除某些字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    # 验证方式二: 自定义验证
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if models.PrettyNum.objects.filter(mobile=mobile).exists():
            raise ValidationError('手机号已存在')
        return mobile