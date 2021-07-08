from django.contrib import admin
from .models import State, City
# Register your models here.

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbvr', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(State, StateAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name', 'state_name', 'zip', 'slug')
    prepopulated_fields = {'slug': ('city_name',)}

admin.site.register(City, CityAdmin)
