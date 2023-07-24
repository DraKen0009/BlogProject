
from django.contrib import admin
from django.urls import path
from . import views
from .views import PostList,PostDetail,PostCreate,PostUpdate,PostDelete,UserPostList
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', PostList.as_view(template_name='blog/home.html'),name='blog-home'),
    path('post/<int:pk>/', PostDetail.as_view(template_name='blog/post_detail.html'),name='post_detail'),
    path('<str:username>/posts/', UserPostList.as_view(template_name='blog/user_posts.html'),name='user_posts'),
    path('create/', login_required(PostCreate.as_view(template_name='blog/post_create.html')),name='post_create'),
    path('post/<int:pk>/update/', login_required(PostUpdate.as_view(template_name='blog/post_update.html')),name='post_update'),
    path('post/<int:pk>/delete/', login_required(PostDelete.as_view(template_name='blog/post_delete.html')),name='post_delete'),
    path('about/', views.about,name='blog-about'),
    ]