from django.shortcuts import render
from .forms import *
from django.views.generic import TemplateView, CreateView, FormView, DetailView
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

class RegisterView(CreateView):
    model = User
    template_name = 'pages/register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'pages/login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        email = form.cleaned_data.get('email')

        password = form.cleaned_data.get('password')
        user = authenticate(email = email,password=password)

        if user is not None:
            if user.is_active:
                login(self.request,user)
                return  redirect('home')
            else:
                return HttpResponse(' Этот пользователь заблокирован')
        else:
            return HttpResponse(' Такого пользователя не существует или данные неправильны')



def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')



class ProfileView(DetailView):
    template_name = 'pages/profile.html'
    model = User
    context_object_name = 'profile'
    queryset = User.objects.all()











