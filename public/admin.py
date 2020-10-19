from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(FuncaoModel)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ('funcao','cbo','criados','modificado','ativo')

