from django.contrib import admin
from .models import itemModels, ativoModels, saidaModels

@admin.register(itemModels)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('Item', 'Quant')

@admin.register(ativoModels)
class ativoAdmin(admin.ModelAdmin):
    list_display = ('Ativo', 'Resp')