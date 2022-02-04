from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from posts.models import Post


def homeView(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "posts/home.html", context)


class HomeView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"


class AddPostView(CreateView):
    model = Post
    template_name = "posts/add_post.html"
    fields = "__all__"
