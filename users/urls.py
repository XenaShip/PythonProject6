from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from .apps import UsersConfig
from .views import RegisterView, ProfileView, MyLogoutView, MyLoginView, email_verification, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),
    path('reset_password/', reset_password, name='reset_password'),
    path('profile/', ProfileView.as_view(template_name='users/profile.html'), name='profile'),
    path('email-confirm/<str:token>/', email_verification, name='email_confirm'),
]