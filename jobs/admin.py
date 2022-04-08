from django.contrib import admin
from .models import Referencias, Jobs

# Register your models here.
"""Permite ao admin, no painel, inserir referencias e jobs manualmente"""

admin.site.register(Jobs)
admin.site.register(Referencias)