from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def index(request):
    # return HttpResponse("Hello World! This page is posts index.")
    # get all objects from Posts
    posts = Post.objects.order_by('-published')
    # using templates
    # args = posts
    return render(request, 'posts/index.html', {'posts': posts})


def post_detail(request, post_id):
    # get function don't allow space between pk and pk-value
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})