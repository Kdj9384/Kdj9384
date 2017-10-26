from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post # Post모델 폼을 적용시킨다.
        fields = ('title', 'text',) # 보여질 Post필드
