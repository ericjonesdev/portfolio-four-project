from . import views
from . models import UserProfiile
from django.urls import path
from .views import UserProfiileDetailView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('user_profile/<slug:username>/', UserProfiileDetailView.as_view(), name='user_profile'),
]