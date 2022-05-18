from django.shortcuts import render
from .models import Post

# Create your views here.
#GET and HTTP protocol =request library

def homepage(request):
    return render(request, 'index.html', {"post": Post.objects.all})