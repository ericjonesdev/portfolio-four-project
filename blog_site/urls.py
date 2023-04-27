from . import views
from . models import UserProfiile
from django.urls import path
from .views import UserProfiileDetailView, UserProfiileUpdateView, UserProfiileDeleteView


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('user_profile/<slug:username>/', UserProfiileDetailView.as_view(), name='user_profile'),
    path('update_profile/<slug:username>/', UserProfiileUpdateView.as_view(), name='update_profile'),
    path('delete_profile/<slug:username>/', UserProfiileDeleteView.as_view(), name='delete_profile'),
]