from django.urls import path
from django.contrib.auth import views as dj_views

from . import views

app_name = 'ivanapp'

urlpatterns = [

    # <---Main Pages

    path('', views.AboutView.as_view(), name='main'),

    # <---User Pages

    # path('user/', views., name='user'),

    # path('user/edit/', views.ProfileUpdate, name='edit'),

    # <---Moder Pages

    # path('advanced/enroll_manager/', views., name='enroll_manager'),

    # <---Admin Pages

    # path('advanced/account_manager', views., name='acc_manager'),

    # <---Auth Pages

    path('login/', views.LoginView.as_view(), name='login'),

    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('register/', views.RegistrationView.as_view(), name='register'),

    # path('changepassword/', views.ChangePasswordView.as_view(), name='changepassword')
]
