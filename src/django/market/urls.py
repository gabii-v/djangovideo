# market/urls.py

from django.urls import path
from .views import (
    CategoriaListCreate, CategoriaDetail,
    EstadoListCreate, EstadoDetail,
    CondicionListCreate, CondicionDetail,
    ArticuloListCreate, ArticuloDetail,
    MensajeListCreate, MensajeDetail,
)

urlpatterns = [
    # Categorías
    path('categorias/', CategoriaListCreate.as_view(), name='categoria-list'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),

    # Estados
    path('estados/', EstadoListCreate.as_view(), name='estado-list'),
    path('estados/<int:pk>/', EstadoDetail.as_view(), name='estado-detail'),

    # Condiciones
    path('condiciones/', CondicionListCreate.as_view(), name='condicion-list'),
    path('condiciones/<int:pk>/', CondicionDetail.as_view(), name='condicion-detail'),

    # Artículos
    path('articulos/', ArticuloListCreate.as_view(), name='articulo-list'),
    path('articulos/<int:pk>/', ArticuloDetail.as_view(), name='articulo-detail'),

    # Mensajes
    path('mensajes/', MensajeListCreate.as_view(), name='mensaje-list'),
    path('mensajes/<int:pk>/', MensajeDetail.as_view(), name='mensaje-detail'),
]
