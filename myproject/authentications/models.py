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



# These are the models that manages the business logic of our Employee Management System.

class Department(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    # Links to the customUser for authentication, but stores staff data here 
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    mobile_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.full_name} ({self.department})"

class Leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    message = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')],
        default='Pending'
    )
    
    def __str__(self):
        return f"Leave for {self.employee.user.full_name} : {self.status}"
    
    