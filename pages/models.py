from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class Faq(models.Model):
    question    = models.CharField(max_length=500)
    author      = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
    )
    answer =      models.TextField()

    def __str__(self):
        return self.question
