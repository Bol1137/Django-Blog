from django.shortcuts import render
from .models import Blog

# Create your views here.

def index(request):
    """A view to render the homepage that contain the list of articles
    and we run small query to retrieve all the blog post
    in our database and then render it on our homepage"""
    blogs =  Blog.objects.all()
    context ={
        'blogs':blogs
    }
    return render(request, 'blog/index.html', context)

def post_detail(request, pk):
    """A view to render each blog post seprately and we 
    do so by grabing the Id of each post and then render it"""
    blog = Blog.objects.get(id = pk)
    context = {
        'blog':blog
    }
    return render(request, 'blog/post_detail.html', context)


def about(request):
    """A simple view to render my about page"""
    return render(request, 'blog/about.html')