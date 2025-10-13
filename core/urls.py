from django.urls import path
from .views import HomePageView, PostCreateView , AboutPageView,PostListView, PostDetailView,PostUpdateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view() , name='create_post'),
    path('about/',  AboutPageView.as_view(), name='about'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
]