from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("Hello World! This page is posts index.")
    # get all objects from Posts
    posts = Post.objects.order_by('-published')
    # using templates
    # args = posts
    return render(request, 'posts/index.html', {'posts': posts})
