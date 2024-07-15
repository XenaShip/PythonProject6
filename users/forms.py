from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from users.models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'phone', 'avatar', 'country')


class UserAuthenticationForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('email', 'password')
