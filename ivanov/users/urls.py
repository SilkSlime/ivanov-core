from django.urls import path, include
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
]
