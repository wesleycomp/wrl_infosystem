from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

class UsuarioView(LoginRequiredMixin, TemplateView):
    template_name = 'page-user.html'

class FuncaoView(LoginRequiredMixin, TemplateView):
        template_name = 'public/funcao.html'