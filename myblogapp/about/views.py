from django.shortcuts import render, get_object_or_404
from .models import Author

def index(request):
    us = get_object_or_404(Author, pk=1)
    return render(request, 'about/index.html', {'us': us})
