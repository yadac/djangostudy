from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Hello World! This page is posts index.")
    # using templates
    return render(request, 'posts/index.html')
