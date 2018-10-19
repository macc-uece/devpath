from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    email = models.EmailField()

    class Meta:
        ordering = ('last_name', 'name')
    
    def __str__(self):
        return ''