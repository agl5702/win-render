from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy
from .managers import CustomUserManager

# Creando mis modelos aquí

class User(AbstractBaseUser,PermissionsMixin):
    first_name = models.CharField(gettext_lazy('First Name'), max_length=100)
    last_name = models.CharField(gettext_lazy('Last Name'), max_length=100)
    email = models.EmailField(gettext_lazy('Email Address'), max_length=254, unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['first_name','last_name']

    objects= CustomUserManager() # Uso del manager 

    class Meta:
        verbose_name = gettext_lazy('User')
        verbose_name_plural = gettext_lazy('Users')

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"