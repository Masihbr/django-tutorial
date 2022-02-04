from django.urls import reverse_lazy

from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from posts.models import Post
from posts.forms import CreatePostForm, UpdatePostForm


def homeView(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/home.html", context)


class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"
    ordering = ["-updated_at", "-created_at"]


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"


class AddPostView(CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "posts/add_post.html"


class UpdatePostView(UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    form_class = UpdatePostForm


class DeletePostView(DeleteView):
    model = Post
    template_name = "posts/delete_post.html"
    success_url = reverse_lazy("home")
