from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

from ckeditor.fields import RichTextField
# Create your models here.


class State(models.Model):
    name        = models.CharField(max_length=100, unique=True)
    abbvr       = models.CharField(max_length=2, unique=True)
    # article     = models.TextField(null=False)
    article     = RichTextField(blank=True, null=True)
    slug        = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('state_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class City(models.Model):
    state_name  = models.ForeignKey('state.State', on_delete=models.CASCADE, related_name='cities')
    city_name   = models.CharField(max_length=50)
    zip         = models.CharField(max_length=10, )
    # city_detail = models.TextField(null=False)
    city_detail = RichTextField(blank=True, null=True)
    slug        = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title+self.state_name)
        return super().save(*args, **kwargs)
