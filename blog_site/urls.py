from . import views
from . models import UserProfiile
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import UserProfiileDetailView, UserProfiileUpdateView, UserProfiileDeleteView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('user_profile/<slug:username>/', UserProfiileDetailView.as_view(), name='user_profile'),
    path('update_profile/<str:username>/', UserProfiileUpdateView.as_view(), name='update_profile'),
    path('delete_profile/<int:pk>/', UserProfiileDeleteView.as_view(), name='delete_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
