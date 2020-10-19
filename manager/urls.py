from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path("pagina/", include('public.urls', namespace='public')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)