from .models import Comment, Post, UserProfiile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfiile
        fields = ['profile_image', 'first_name', 'last_name', 'bio', 'dob', 'location', 'github', 'website', 'twitter', 'occupation']