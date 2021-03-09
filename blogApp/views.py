from django.shortcuts import render, get_object_or_404
from blogApp.models import Post, Category


# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'blogApp/blog.html', {'posts': posts, "categories": categories})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blogApp/category.html', {'category': category, 'posts': posts})
