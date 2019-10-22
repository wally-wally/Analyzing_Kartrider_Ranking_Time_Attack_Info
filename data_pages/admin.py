from django.contrib import admin
from .models import DataPage

# Register your models here.
class DataPageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'nickname', 'speed', 'created_at',)

admin.site.register(DataPage, DataPageAdmin)
