# from django.db import models

# # Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)

from django.db import models

# Corrected User model without the default value for 'user_id'
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)  # Consider using Django's User model for handling passwords securely
    user_role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.user_role} - {self.email})"

class The_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='admin')
    
    def __str__(self):
        return f"{self.user.name} (Admin - {self.user.email})"

class The_Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='trainer')
    
    def __str__(self):
        return f"{self.user.name} (Trainer - {self.user.email})"

class The_Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='client')
    
    def __str__(self):
        return f"{self.user.name} (Client - {self.user.email})"
