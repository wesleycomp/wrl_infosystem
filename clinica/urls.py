from django.urls import path, re_path
#from .views import *
from clinica import views

urlpatterns = [
    #path('', IndexView.as_view()),
    path('', views.index, name='home'),
]