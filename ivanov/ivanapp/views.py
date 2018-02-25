from django.shortcuts import redirect, render, get_object_or_404

from django.urls import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm

from django.contrib.auth.models import User

from django.views import generic

from django.contrib.auth.models import User


# <-- Main Views


class AboutView(generic.TemplateView):
    template_name = "about.html"


class EnrollView(generic.TemplateView):
    template_name = "enroll.html"


# <-- User Views


# class ProfileUpdateView(generic.UpdateView):
#     form_class = PasswordChangeForm
#     success_url = reverse_lazy('ivanapp:changepassword')
#     template_name = 'auth/change_password.html'


# <-- Auth Views


# class ChangePasswordView(generic.FormView):



class RegistrationView(generic.FormView):
    form_class = UserRegistrationForm
    template_name = "auth/register.html"
    success_url = reverse_lazy('ivanapp:login')

    def form_valid(self, form):
        user = form.save()
        print(form.cleaned_data)


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('ivanapp:main')
    template_name = 'auth/login.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)


class LogoutView(generic.RedirectView):
    url = reverse_lazy('ivanapp:main')
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
