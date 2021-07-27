from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField



class Faq(models.Model):
    question    = models.CharField(max_length=500)
    author      = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
    )
    answer      = RichTextField(blank=True, null=True)
    slug        = models.SlugField(null=True, unique=True)


    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('faq_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.question)
        return super().save(*args, **kwargs)
