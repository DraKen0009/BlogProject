from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

# def home(request):
#     posts=Post.objects.all()
#     context={
#         'posts':posts
#     }
#     return render(request,'blog/home.html',context)

class PostList(ListView):
    model = Post
    ordering = ['-post_date']
    context_object_name = 'posts'
    paginate_by = 5
    print(Post.objects.all())

class UserPostList(ListView):
    model = Post
    ordering = ['-post_date']
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user=User.objects.get(username=self.kwargs.get('username'))
        return Post.objects.filter(post_author=user)

class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(CreateView):
    model = Post
    fields = ['post_title','post_content']

    def form_valid(self, form):
        form.instance.post_author=self.request.user
        return super().form_valid(form)

class PostUpdate(UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['post_title','post_content']

    def form_valid(self, form):
        form.instance.post_author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.post_author:
            return True
        else:
            return False

class PostDelete(UserPassesTestMixin,DeleteView):
    model = Post

    success_url = reverse_lazy('blog-home')

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.post_author:
            return True
        else:
            return False


def about(request):

    return render(request,'blog/about.html')