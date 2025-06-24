from django.shortcuts import render
from rest_framework import generics
from .models import Categoria, Estado, Condicion, Articulo, Mensaje
from .serializers import (
    CategoriaSerializer, EstadoSerializer, CondicionSerializer,
    ArticuloSerializer, MensajeSerializer, ArticuloConRelacionesSerializer,
    MensajeSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# -------- CATEGORIA --------
class CategoriaListCreate(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# -------- ESTADO --------
class EstadoListCreate(generics.ListCreateAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class EstadoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

# -------- CONDICION --------
class CondicionListCreate(generics.ListCreateAPIView):
    queryset = Condicion.objects.all()
    serializer_class = CondicionSerializer

class CondicionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Condicion.objects.all()
    serializer_class = CondicionSerializer

# -------- ARTICULO --------
#class ArticuloListCreate(generics.ListCreateAPIView):
#    queryset = Articulo.objects.all()
#    serializer_class = ArticuloSerializer

#class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Articulo.objects.all()
#    serializer_class = ArticuloSerializer

# Artículo (con datos legibles y anidados)
class ArticuloListCreate(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloConRelacionesSerializer
    permission_classes = (IsAuthenticated,)

class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloConRelacionesSerializer
    permission_classes = (IsAuthenticated,)

# -------- MENSAJE --------
#class MensajeListCreate(generics.ListCreateAPIView):
#    queryset = Mensaje.objects.all()
#    serializer_class = MensajeSerializer

#class MensajeDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Mensaje.objects.all()
#    serializer_class = MensajeSerializer

# Mensaje
class MensajeListCreate(generics.ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = (IsAuthenticated,)

class MensajeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = (IsAuthenticated,)