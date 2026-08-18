from django.db import models

from authentications.models import CustomUser

# Create your models here.


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
    