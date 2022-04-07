from django.contrib import admin

# Register your models here.
from .models import Cat, CatToy # import the Cat model from models.py
# Register your models here.

admin.site.register(Cat)

admin.site.register(CatToy)