from django.contrib import admin
from .models import State
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbvr', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(State, StateAdmin)
