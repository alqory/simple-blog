from django.urls import path
from django.views.generic import TemplateView

from .views import *

app_name = 'blog'

urlpatterns = [
    path('',ArtikelView.as_view(), name='index'),
    path('<slug>/',ArtikelDetail.as_view(), name='detail'),
    path('kategori/<category>', ArtikelKategoriView.as_view(), name='kategori'),
    path('tambah', ArtikelCreate.as_view(), name='tambah'),
    path('manage', ArtikelManage.as_view(), name='manage'),
    path('manage/hapus/<pk>', ArtikelHapus.as_view(), name='hapus'),
    path('manage/update/<pk>', ArtikelUpdate.as_view(), name='update')
]