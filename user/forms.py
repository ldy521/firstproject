from django import forms
from user.models import User


class RegisterForm(forms.ModelForm):# 和model关联的form
    class Meta:
        # 指定一个model
        model = User
        # 需要验证的字段
        fields = ['nickname','password','age','sex','icon']
    # 缺什么补什么
    password2 = forms.CharField(max_length=128)

    def clean_password2(self):
        '''检查两次输入的密码是否一致'''
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('两次输入的密码不一致')