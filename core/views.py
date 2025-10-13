from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView




class HomePageView(TemplateView):
    template_name = 'home.html'


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)





class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        post.delete()
        return redirect('posts')


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('posts')


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('posts')



# class PostDeleteView(DeleteView):
#     model = Post
#     template_name = 'post_delete.html'
#     success_url = reverse_lazy('posts')


    








#     def posts_view(request):
#     search_text = request.GET.get('search')
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request,'posts.html',context)




# def post_detail_view(request, id):

#     context = {
#         'post': Post.objects.get(id=id)
#     }

#     return render(request,'post_detail.html', context)


# def home_view(request):
#     return render(request, 'home.html')




# def create_post_view(request):
#     if request.method == 'POST': 
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')
#     else:
#         form = PostForm()
        

#     context = {
#         'form': form
    
#     }

#     return render(request, 'create_post.html', context)
