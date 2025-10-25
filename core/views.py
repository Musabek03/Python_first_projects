from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post,Category,User, UserPostAction,Comment
from .forms import PostForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages



class HomePageView(TemplateView):
    template_name = 'home.html'


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['authors'] = User.objects.all()
        return context
    
    def  get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        category = self.request.GET.get('category', '')
        author = self.request.GET.get('author', '')
        if search:
            queryset = queryset.filter(title__icontains=search) 
        if category:
            queryset = queryset.filter(category__id=category)
        if author:
            queryset = queryset.filter(user__id=author)
        return queryset.filter(is_published=True).order_by('-created_at')
    
   

    


    # def get_queryset(self):
    #     return Post.objects.filter(is_published=True)



class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        UserPostAction.objects.get_or_create(user=request.user, post=self.object)
        return response
    
    

    def post(self, request, *args, **kwargs):
        post = self.get_object()    
        if post.user != request.user:
            messages.error(request, "Siz bul postti oshire almaysiz!")
            return redirect('post_detail', pk=post.pk)
        post.delete()
        return redirect('posts')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['popular_posts'] = self.model.objects.filter(is_published=True)[:5]
        return context
    
    
        

class PostCreateView(PermissionRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('posts')
    permission_required = 'core.add_post'


    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    




class AboutPageView(TemplateView):
    template_name = 'about.html'


class PostUpdateView(PermissionRequiredMixin,UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    success_url = reverse_lazy('posts')
    permission_required = 'core.change_post'

    def form_valid(self, form):
        if form.instance.user != self.request.user:
            form.add_error(None, "Siz bul posttı jańalay almaýsız.")
            return self.form_invalid(form)
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

    # def def form_valid(self, form):
    #     if form self.object.user = self.request.user
    #     return super().form_valid(form)
    

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
