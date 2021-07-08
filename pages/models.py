from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.

class State(models.Model):
    name    = models.CharField(max_length=100)
    abbvr   = models.CharField(max_length=2, unique=True)
    article = models.TextField(null=False)
    slug    = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('state_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


# class City(models.Model):
#     city_name   = models.CharField(max_length=50)
#     # state_name  = models.ForeignKey('state.name', on_delete=models.CASCADE,)
#     zip         = models.CharField(max_length=5, unique=True)
#     city_detail = models.TextField(null=False)
#     slug        = models.SlugField(null=False, unique=True)
#
#     def __str__(self):
#         return self.city_name


class Faq(models.Model):
    question    = models.CharField(max_length=500)
    author      = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
    )
    answer =      models.TextField()

    def __str__(self):
        return self.question
