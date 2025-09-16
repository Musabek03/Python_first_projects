from django.urls import path
from .views import home_view, posts_view, post_detail_view  


urlpatterns = [
    path('', home_view, name='home'),  
    path('posts/', posts_view, name='posts'),
    path('posts/<int:id>/', post_detail_view, name='post_detail'),
]