from django.contrib import admin
from .models import Profile

# Register the Profile model with the admin site to make it manageable through the Django admin interface
admin.site.register(Profile)
