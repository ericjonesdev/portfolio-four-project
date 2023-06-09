from django.contrib import admin
from .models import Post, Comment, UserProfiile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''
    Administrative function to allow site admin to display, list and filter 
    posts.
    '''
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'author', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Administrative function to allow site admin to display, list, approve and
    filter comments.
    '''

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(UserProfiile)
class UserProfileAdmin(admin.ModelAdmin):
    '''
    Administrative function to allow site admin to display & view user
    information.
    '''

    list_display = (
        'user',
        'bio',
        'github',
    )
