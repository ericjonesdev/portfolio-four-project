from .models import Comment, Post, UserProfiile
from django import forms
from django_summernote.widgets import SummernoteWidget


class CommentForm(forms.ModelForm):
    '''
    sets the model parameter for the comment form field    
    '''
    class Meta:
        model = Comment
        fields = ('body',)
        

class UserProfileForm(forms.ModelForm):
    '''
    sets the parameters for the user profile form view   
    '''
    class Meta:
        model = UserProfiile
        fields = ('profile_image', 'first_name', 'last_name', 'bio', 'dob', 'location', 'github', 'website', 'twitter', 'occupation')


class PostForm(forms.ModelForm):
    '''
    sets the parameters for the user profile form view   
    '''
    status = forms.ChoiceField(choices=(('Draft', 'Draft'), ('Published', 'Published')), widget=forms.RadioSelect())

    class Meta:
        '''
        adds functionality for summernote WYSIWYG editor to be used
        within registered user comments   
        '''
        model = Post
        fields = ('title', 'slug', 'content', 'featured_image', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

