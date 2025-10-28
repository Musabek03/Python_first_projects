from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post,Category,User, UserPostAction,Comment
from .forms import PostForm
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta





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
    
   


class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'
    

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        user_post_action, created = UserPostAction.objects.get_or_create(user=request.user, post=self.object)
        if not created:
            dt = timezone.now() - user_post_action.updated_at   
            max_time_delta = timedelta(minutes=5)
            if dt > max_time_delta:
                user_post_action.view_count += 1
                user_post_action.save()
              
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
        #context['user_post_action'] = self.object.user_actions.get(user=self.request.user) Usi kodtin ornina tomendegini jazdim
        context['user_post_action'] = self.object.user_actions.filter(user=self.request.user).first()
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



class UserActionUpdateView(LoginRequiredMixin, UpdateView):
    model = Post

    def post(self, request, *args, **kwargs):
        form_data = request.POST
        post = self.get_object()
        action = form_data.get('action')
        user_post_action = post.user_actions.get(user=request.user)
        if action == 'like':
            user_post_action.liked = True
            user_post_action.disliked = False
        elif action == 'dislike':
            user_post_action.liked = False
            user_post_action.disliked = True
        user_post_action.save()
        return redirect('post_detail', pk=post.id)
    



class UserActionComment(LoginRequiredMixin, DetailView):
    template_name = 'post_detail.html' 
    model = Post
    
    def post(self, request, *args, **kwargs):
        
        post = self.get_object()

        if "delete_comment_id" in request.POST:
            comment_id = request.POST.get("delete_comment_id")
            comment = Comment.objects.get(id=comment_id)

            if comment.user != request.user and not request.user.is_superuser: 
                messages.error(request, "Siz bul kommentti oshire almaysiz!")
                return redirect('post_detail', pk=post.pk)
            comment.delete()

        text = request.POST.get('comment_text')
        if text:
            comment = Comment.objects.create(post=post, user=request.user, text=text)
            comment.save()

        return redirect('post_detail', pk=post.id)
    

    


    

