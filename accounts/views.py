from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import SignupForm


class SignUpView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user