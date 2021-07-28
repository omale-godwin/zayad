from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    con = Blog.objects.all()
    context = {
        'blog': con
    }

    return render(request, 'blog/blog.html', context)

def blogdetail(request, blog_id):

    listing = get_object_or_404(Blog, pk=blog_id)
    context = {
    'blog': listing
    }
    return render(request, 'blog/blogdetail.html', context)