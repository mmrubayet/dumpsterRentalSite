from django.contrib import admin
from .models import Faq, State
# Register your models here.

admin.site.register([Faq, State])
