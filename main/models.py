# from django.db import models

# # Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, default='password')
    user_role = models.CharField(max_length=50, default='client')

    def __str__(self):
        return f"{self.name} ({self.user_role})"

class The_Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='admin')

class The_Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='trainer')

class The_Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='client')
