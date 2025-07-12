# market/urls.py

from django.urls import path, include
from .views import (
    CategoriaListCreate, CategoriaDetail,
    EstadoListCreate, EstadoDetail,
    CondicionListCreate, CondicionDetail,
    ArticuloListCreate, ArticuloDetail,
    MensajeListCreate, MensajeDetail,
)
from .views import RegisterView
from .views import UsuarioAutenticadoView
from .views import PerfilUsuarioView

from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)

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

    path('auth/register/', RegisterView.as_view(), name='register'),

    path('usuarios/me/', UsuarioAutenticadoView.as_view(), name='usuario-me'),

    path('usuarios/perfil/', PerfilUsuarioView.as_view(), name='perfil-usuario'),

    path('api/', include(router.urls)),
]
