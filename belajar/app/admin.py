from django.contrib import admin
from .models import book, user

# Register your models here.
admin.site.register(user)
admin.site.register(book)