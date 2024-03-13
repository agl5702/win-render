from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


# Class User creation form
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=User
        fields=['email','first_name','last_name']
        error_class='error'

# Class User change form
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=User
        fields=['email','first_name','last_name']
        error_class='error'