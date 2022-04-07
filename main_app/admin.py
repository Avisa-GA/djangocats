from django.contrib import admin

# Register your models here.
from .models import Cat # import the Cat model from models.py
# Register your models here.

admin.site.register(Cat)