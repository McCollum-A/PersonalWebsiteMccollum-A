from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.
def allblogs(request):
    AllBlogs = Blog.objects.all()
    return render(request, 'BlogApp/AllBlogs.html', {'AllBlogs': AllBlogs})


def blogentire(request, Blog_id):
    BlogEntire = get_object_or_404(Blog, pk=Blog_id)
    return render(request, 'BlogApp/Entire.html', {'BlogEntire': BlogEntire})
