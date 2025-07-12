from django.shortcuts import render
from rest_framework import generics
from .models import Categoria, Estado, Condicion, Articulo, Mensaje
from .serializers import (
    CategoriaSerializer, EstadoSerializer, CondicionSerializer,
    ArticuloSerializer, MensajeSerializer, ArticuloConRelacionesSerializer,
    MensajeSerializer
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer

from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from .models import Perfil
from .serializers import PerfilSerializer
from rest_framework.generics import RetrieveUpdateAPIView

from .serializers import UsuarioSerializer  # Lo definimos abajo

from rest_framework import viewsets


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
#class ArticuloListCreate(generics.ListCreateAPIView):
#    queryset = Articulo.objects.all()
#    serializer_class = ArticuloConRelacionesSerializer
#    #permission_classes = (IsAuthenticated,)
#    permission_classes = (IsAuthenticatedOrReadOnly,)

class ArticuloListCreate(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArticuloSerializer
        return ArticuloConRelacionesSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloConRelacionesSerializer
    #permission_classes = (IsAuthenticated,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

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

    def perform_create(self, serializer):
        print("DATA ENVIADA AL SERIALIZER:")
        print(self.request.data)
        serializer.save(emisor=self.request.user)


class MensajeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = (IsAuthenticated,)


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Usuario creado con éxito"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

#class UsuarioAutenticadoView(APIView):
#    permission_classes = [IsAuthenticated]
#
#    def get(self, request):
#        serializer = UsuarioSerializer(request.user)
#        return Response(serializer.data)
    
class UsuarioAutenticadoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
class PerfilUsuarioView(RetrieveUpdateAPIView):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.perfil
    
class UsuarioMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UsuarioSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer