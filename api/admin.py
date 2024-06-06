from atexit import register
from django.contrib import admin
from .models import Data

# Register your models here.

@admin.register(Data)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Data._meta.get_fields()]
