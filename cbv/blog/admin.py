from django.contrib import admin
from .models import *

# Register your models here.
class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = ['published','update','slug']

admin.site.register(Artikel, ArtikelAdmin)