from django.shortcuts import render
from blogApp.models import Post


# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, 'blogApp/blog.html', {'posts': posts})
