from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, "posts/posts.html", {
        'posts': posts
    })

def show(request, id):
    post = Post.objects.get(id=id)
    return render(request, "posts/post.html", {
        'post': post
    })
