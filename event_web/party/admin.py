from django.contrib import admin
from .models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'id']
    list_display_links = ['name', 'last_name', 'id']


admin.site.register(Person, PersonAdmin)
