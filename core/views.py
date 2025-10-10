from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


# Create your views here.

def home_view(request):
    return render(request, 'home.html')


def posts_view(request):
    search_text = request.GET.get('search')
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'posts.html',context)



def post_detail_view(request, id):

    context = {
        'post': Post.objects.get(id=id)
    }

    return render(request,'post_detail.html', context)

def create_post_view(request):
    if request.method == 'POST': 
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = PostForm()
        
    

    context = {
        'form': form
    
    }

    return render(request, 'create_post.html', context)