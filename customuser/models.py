from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Profile(AbstractUser):
    descr = models.TextField(max_length=500,blank=True)
    contact = models.TextField(max_length=12,blank=True)
    doctor = models.BooleanField(default=False)
    def __str__(self):
        return self.username