from django.urls import path, include
from .views import UserRegistrationView, UserLoginView, logout_view

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
