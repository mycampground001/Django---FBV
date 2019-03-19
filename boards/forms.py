from django import forms
from .models import Board

# class BoardForm(forms.Form):
#     title = forms.CharField(label="제목", max_length=10,
#                             error_messages={"required":"제목써라"}
#                             )
                            
                            
#     content = forms.CharField(label="내용", 
#                             error_messages={"required":"내용써라"},
#                             widget=forms.Textarea(attrs={
#                                 'placeholder':"내용쓰자",
#                                 'class':'input-box'
#                             })
#                             )
                            
# modelform
# 중복제거를 위한. 모델이 있는경우 이런경우는 편하게...
class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = '__all__'
        fields = ['title','content']
        widgets = {'title': forms.TextInput(attrs={
                                            'placeholder':'제목써라',
                                            'class':'title'
                                            }),
                    'content':forms.Textarea(attrs={
                                            'placeholder':'내용써라',
                                            'class':'content'
                                            })
                    }
    
        error_messages = {'title':{
                                'required':'제목은 반드시 써라'
                                },
                            'content': {
                                    'required':'내용은 반드시 써라'
                            }
                        }