from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'slug')
    prepopulated_fields = {'slug': ('question',)}


admin.site.register(Faq, FaqAdmin)
