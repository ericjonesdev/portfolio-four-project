from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields =  user.Meta.get_fields(include_parents=True, include_hidden=False)