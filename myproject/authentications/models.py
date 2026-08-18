from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
# Create your models here.

# PermissionsMixin is an abstract model class that provides the database fields and methods necessary to fully support Django's built-in permission and group framework.

#It adds is_superuser, groups and user_permission.
# It also has methods has_perm, get_user_permission and more.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']
    
    def __str__(self):
        return self.email
    

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"Profile for {self.user.email}"

# The CustomUser manages authentication, while the Profile model holds non-sensitive metadata via a OneToOneField




    