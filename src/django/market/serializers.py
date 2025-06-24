# market/serializers.py

from rest_framework import serializers
from .models import Categoria, Estado, Condicion, Articulo, Mensaje
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class CondicionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condicion
        fields = '__all__'

class ArticuloSerializer(serializers.ModelSerializer):
    usuario_username = serializers.ReadOnlyField(source='usuario.username')
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    estado_descripcion = serializers.ReadOnlyField(source='estado.descripcion')
    condicion_descripcion = serializers.ReadOnlyField(source='condicion.descripcion')

    class Meta:
        model = Articulo
        fields = [
            'id',
            'titulo',
            'descripcion',
            'fecha_publicacion',
            'usuario',
            'usuario_username',
            'categoria',
            'categoria_nombre',
            'estado',
            'estado_descripcion',
            'condicion',
            'condicion_descripcion',
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ArticuloConRelacionesSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    estado = EstadoSerializer(read_only=True)
    condicion = CondicionSerializer(read_only=True)

    class Meta:
        model = Articulo
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    emisor_username = serializers.ReadOnlyField(source='emisor.username')
    receptor_username = serializers.ReadOnlyField(source='receptor.username')
    articulo_titulo = serializers.ReadOnlyField(source='articulo.titulo')

    class Meta:
        model = Mensaje
        fields = [
            'id',
            'emisor',
            'emisor_username',
            'receptor',
            'receptor_username',
            'articulo',
            'articulo_titulo',
            'contenido',
            'fecha_envio',
        ]

