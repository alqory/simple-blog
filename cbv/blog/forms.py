from django import forms
from django.forms import ModelForm, widgets
from .models import *

class ArtikelForm(ModelForm):
    class Meta:
        model = Artikel
        fields = ['judul','isi','kategori']

   