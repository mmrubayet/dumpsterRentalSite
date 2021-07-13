from django.contrib import admin
from .models import Faq


class PagesAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbvr', 'article',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Faq)
