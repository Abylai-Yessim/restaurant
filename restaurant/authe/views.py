from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import  logout, login
from django.urls import reverse_lazy
from .forms import *
import sys
sys.path.append("..")
from back.models import *
# Create your views here.

class SignUpUser(CreateView):
    form_class = SignUpUserForm
    template_name = 'authe/signup.html'
    success_url = reverse_lazy('back:reviews')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Регистрация'

        return context
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('back:home')
    

class SignInUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'authe/signin.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Вход'

        return context
    
    def get_success_url(self):
        return reverse_lazy('back:home')
    
def signout_user(request):
    logout(request)
    return redirect('back:home')