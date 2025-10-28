from django.urls import path
from .views import HomePageView, PostCreateView , AboutPageView,PostListView, PostDetailView,PostUpdateView,UserActionUpdateView,UserActionComment


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view() , name='create_post'),
    path('about/',  AboutPageView.as_view(), name='about'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/user_action_update/', UserActionUpdateView.as_view(), name='user_action_update'),
    path('posts/<int:pk>/user_action_comment/',UserActionComment.as_view(), name='user_action_comment'),
]