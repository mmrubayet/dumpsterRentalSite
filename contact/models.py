from django.db import models
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name        = models.CharField(max_length=255)
    email       = models.EmailField()
    phone       = models.CharField(max_length=255)
    location    = models.CharField(max_length=255)
    message     = models.TextField()
    received    = models.DateTimeField(auto_now_add=True) #default= timezone.now

    def __str__(self):
        return self.name
