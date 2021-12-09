from blog.models import *
from django.views.generic import TemplateView
from blog.views import KategoriArtikel

class HomeBaseView(TemplateView, KategoriArtikel):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data_list'] = self.get_latest_artikel()

        return context
        