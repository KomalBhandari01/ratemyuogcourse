from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.userName