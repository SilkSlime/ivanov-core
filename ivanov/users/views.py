from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.models import User
from .forms import UserLoginForm


@login_required
def logout_view(request):
    logout(request)
    return redirect('/')


class UserRegistrationView(CreateView):
    model = User
    template_name = 'registration.html'
    fields = ['username', 'password']
    success_url = '/users/login/'
    
    def form_valid(self, form):
        user = User(username = form.cleaned_data['username'])
        user.set_password(form.cleaned_data['password'])
        user.save()
        return redirect(self.success_url)


class UserLoginView(FormView):
    template_name = 'login.html'
    form_class = UserLoginForm
    success_url = '/'
    
    def post(self, request, *args, **kwargs):
        self.request = request
        return super(UserLoginView, self).post(request, *args, **kwargs)
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)
        return redirect(self.success_url)