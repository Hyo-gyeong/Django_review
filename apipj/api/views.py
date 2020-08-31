from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .form import APIpost

# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request, 'home.html', {'blog':blog})

def detail(request, blog_id):
    blog = get_object_or_404 (Blog, pk = blog_id)
    return render(request, 'detail.html', {'detail':blog})

def new(request):
    if request.method == 'POST':
        form = APIpost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/detail/' + str(post.id))
    else:
        form = APIpost()
        return render(request, 'new.html', {'form':form})
            
def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        form = APIpost(request.POST, instance=blog)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/detail/' + str(blog.id))
    else:
        form = APIpost(instance = blog)
        return render(request, 'new.html', {'form':form})