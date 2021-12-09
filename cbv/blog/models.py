from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Artikel(models.Model):
    judul       = models.CharField(max_length=255)
    isi         = models.TextField()
    kategori    = models.CharField(max_length=225)
    published   = models.DateTimeField(auto_now_add=True)
    update      = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(blank=True, editable=False, max_length=255)


    """
    Fungsi get absolute url, Pada createForm saat data mau di simpan, dia perlu meng-redirect
    ke url detail nya.
    
    """
    def get_absolute_url(self):
       return reverse('blog:detail', kwargs={"slug": self.slug})

    def save(self):
        self.slug = slugify(self.judul)
        super().save()

    def __str__(self):
        return self.judul
    