import random
import secrets
import string

from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView
from users.forms import RegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http:/{host}/users/email-confirm/{token}/'
        send_mail(subject="Подтвердите почту",
                  message=f"Чтобы подтвердить почту, перейдите по ссылке {url}",
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email, ]
                  )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    context = {
        'success_message': 'Новый пароль выслан на вашу почту.',
    }
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        characters = string.ascii_letters + string.digits
        characters_list = list(characters)
        random.shuffle(characters_list)
        password = ''.join(characters_list[:10])
        user.set_password(password)
        user.save()

        send_mail(
            subject='Смена пароля',
            message=f'Ваш новый пароль: {password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return render(request, 'users/reset_password.html', context)
    return render(request, 'users/reset_password.html')






class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class MyLogoutView(LogoutView):
    model = User
    form_class = RegisterForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')

    def logout_view(request):
        logout(request)
        return redirect("/")


class MyLoginView(LoginView):
    model = User
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:product_list')

