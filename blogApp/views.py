from django.shortcuts import render
from blogApp.models import Post, Category


# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blogApp/blog.html', {'posts': posts, "categories": categories})


def category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blogApp/category.html', {'category': category, 'posts': posts})
