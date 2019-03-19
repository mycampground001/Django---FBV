from django import forms
from .models import Board

class BoardForm(forms.Form):
    title = forms.CharField(label="제목", max_length=10,
                            error_messages={"required":"제목써라"}
                            )
                            
                            
    content = forms.CharField(label="내용", 
                            error_messages={"required":"내용써라"},
                            widget=forms.Textarea(attrs={
                                'placeholder':"내용쓰자",
                                'class':'input-box'
                            })
                            )