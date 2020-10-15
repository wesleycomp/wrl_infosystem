from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('user', UsuarioView.as_view(), name='usuario'),
    path('funcao', FuncaoView.as_view(), name='funcao'),
]