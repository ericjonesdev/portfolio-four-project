from .models import Comment, Post, UserProfiile
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfiile
        fields = ('profile_image', 'first_name', 'last_name', 'bio', 'dob', 'location', 'github', 'website', 'twitter', 'occupation')


class PostForm(forms.ModelForm):
    status = forms.ChoiceField(choices=(('Draft', 'Draft'), ('Published', 'Published')), widget=forms.RadioSelect())

    class Meta:
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

