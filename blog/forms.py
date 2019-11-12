from django import forms
from .models import Post

class PostForm(forms.ModelForm): # PostForm이라는 폼 정의

    class Meta:
        model = Post            # 폼에서 사용할 모델을 지정
        fields = ('title', 'text',) # 폼에 등장할 필드 지정
