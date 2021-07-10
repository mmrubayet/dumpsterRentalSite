from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Faq(models.Model):
    question    = models.CharField(max_length=500)
    author      = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
    )
    # answer      = models.TextField()
    answer      = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('faq_detail', args=[str(self.id)])
