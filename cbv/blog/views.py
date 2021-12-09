from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls.base import reverse_lazy

from .models import *
from .forms import *

class KategoriArtikel:
    model = Artikel

    def get_latest_artikel(self):
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []

        for kategori in kategori_list:
            artikels = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikels)
        return queryset

class ArtikelUpdate(UpdateView):
    template_name = 'update'
    form_class = ArtikelForm
    model = Artikel
    template_name = 'update.html'

class ArtikelHapus(DeleteView):
    model = Artikel
    template_name = 'hapus.html'
    success_url = reverse_lazy('blog:manage')
    context_object_name = 'artikel_data'

class ArtikelManage(ListView):
    model = Artikel
    template_name = 'manage.html'
    context_object_name = 'artikel_list'


class ArtikelCreate(CreateView):
    model = Artikel
    form_class = ArtikelForm
    template_name = 'tambah_artikel.html'
    

class ArtikelKategoriView(ListView):
    model = Artikel
    context_object_name = 'Artikel_list'
    template_name='artikel_kategori.html'
    paginate_by = 3
    ordering = ['-published']

    def get_queryset(self, **kwargs):
        return Artikel.objects.filter(kategori=self.kwargs.get('category'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # context['kategori'] = self.model.objects.get(kategori=self.kwargs.get('kategori'))
        context['kategori_list'] = self.model.objects.values_list('kategori', flat=True).distinct().exclude(kategori=self.kwargs.get('kategori'))
        return context

class ArtikelView(ListView):
    model = Artikel
    context_object_name = 'Artikel_list'
    template_name   ='index.html'
    paginate_by = 3
    ordering = ['-published']

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['kategori_list'] = self.model.objects.values_list('kategori', flat=True).distinct()
        return context

    def get_queryset(self):
        query = self.request.GET.get('artikel')
        if query:
            object_list = self.model.objects.filter(judul__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

        

class ArtikelDetail(DetailView):
    model = Artikel
    template_name='detail.html'
    context_object_name = 'Detail_list'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['kategori_list'] = self.model.objects.values_list('kategori', flat=True).distinct()
        context['kategori_serupa'] = self.model.objects.filter(kategori = self.object.kategori).exclude(slug=self.object.slug)
        # print(self.object.kategori)
        return context