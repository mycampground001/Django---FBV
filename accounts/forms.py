from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.conf import settings
# Django	
# UserCreationForm	    회원가입
# AuthenticationForm	로그인
# UserChangeForm	    회원변경
# PasswordChangeForm	비밀번호변경
	
# class UserForm(forms.ModelForm):
    # class Meta:
        # model = get_user_model()
        # fields = ["username","password"]

class UserCustomCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username','password1','password2','email')

class UserCustomChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('username','email','first_name','last_name')