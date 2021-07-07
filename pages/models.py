from django.db import models

# Create your models here.

class State(models.Model):
    name    = models.CharField(max_length=100)
    abbvr   = models.CharField(max_length=2)
    article = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Faq(models.Model):
    question    = models.CharField(max_length=500)
    author      = models.ForeignKey(
            'auth.user',
            on_delete=models.CASCADE,
    )
    answer =      models.TextField()

    def __str__(self):
        return self.question
