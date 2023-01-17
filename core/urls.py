from django.urls import path
from .views import ItemViews, AtivoViews, SaidaViews, listAtivosViews, \
    listItemViews, listSaidaViews, alterItemViews, alterAtivoViews, deleteItemViews, deleteAtivoViews

urlpatterns = [
    path('item/', ItemViews, name='item.html'),
    path('ativo/', AtivoViews, name='ativo.html'),
    path('', SaidaViews, name='saida.html'),
    path('ativo/listativos/', listAtivosViews, name='listativos.html'),
    path('item/listitem/', listItemViews, name='listitem.html'),
    path('listsaida/', listSaidaViews, name='listsaida.html'),
    path('item/<int:id>/', alterItemViews, name='alterItemViews'),
    path('deleteitem/<int:id>', deleteItemViews, name='deleteItemViews'),
    path('ativo/<int:id>/', alterAtivoViews, name='alterAtivoViews'),
    path('deleteativo/<int:id>/', deleteAtivoViews, name='deleteAtivoViews')
]