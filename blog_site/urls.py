from . import views
from . models import UserProfiile
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserProfiileDetailView, UserProfiileUpdateView, UserProfiileDeleteView, UserBlogPostListView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create_post/', views.UserBlogPostCreateView.as_view(), name='create_post'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('user_profile/<int:user_pk>/', views.UserProfiileDetailView.as_view(), name='user_profile'),
    path('update_profile/<str:username>/', views.UserProfiileUpdateView.as_view(), name='update_profile'),
    path('delete_profile/<int:pk>/', views.UserProfiileDeleteView.as_view(), name='delete_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('<slug:slug>/edit/', views.UserBlogPostUpdateView.as_view(), name='edit_post'),
    path('user_post_list/', views.UserBlogPostListView.as_view(), name='user_post_list'),
]
