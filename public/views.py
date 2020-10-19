from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *

class FuncaotListView(ListView):
    model = FuncaoModel
    template_name = 'funcao/list.html'

class ContactDetailView(DetailView):
    model = FuncaoModel

class ContactCreateView(CreateView):
    model = FuncaoModel

class ContactUpdateView(UpdateView):
    model = FuncaoModel

class ContactDeleteView(DeleteView):
    model = FuncaoModel


