 #声明用户表单
import re

from django import forms
from django.core.exceptions import ValidationError

from user.models import UserProfile


class UserProfileForm(forms.ModelForm):
    # 声明model模型中不存在的属性
    password2 = forms.CharField(max_length=50,
                                label='重复口令',
                                required=False)

    class Meta:
        model = UserProfile
        fields = '__all__'
        error_messages = {
            'username':
                {'required': '用户名不能为空'},
            'password': {
                'required': '口令不能为空'
            },
            'email': {
                'required': '邮箱不能为空'
            },
            'phone': {
                'required': '电话不能为空',
                'max_length': '电话号码长度不能超过12字符'
            }
        }

    # 验证phone的数据
    def clean_phone(self):

        # 从"干净"的数据字典中获取phone数据
        phone = self.cleaned_data.get('phone')
        if re.match(r'1[357-9]\d{9}', phone):
            return phone
        else:
            raise ValidationError('手机号格式有错误')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password2 == None or len(password2)==0:
            raise ValidationError('重复口令不能为空')

        if password2 != password:
            raise ValidationError('两次口令不相同')
        return password





