from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User

# Create your views here.


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


class UserLoginView(CreateView):
    model = User
    success_url = 'kek'