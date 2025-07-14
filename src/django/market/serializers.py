# market/serializers.py

from rest_framework import serializers
from .models import Categoria, Estado, Condicion, Articulo, Mensaje
from django.contrib.auth.models import User
from .models import Perfil


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
            'precio',
            'fecha_publicacion',
            'usuario',
            'usuario_username',
            'categoria',
            'categoria_nombre',
            'estado',
            'estado_descripcion',
            'condicion',
            'condicion_descripcion',
            'esta_activo',
            'vendido',
        ]
        read_only_fields = ['usuario', 'fecha_publicacion']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ArticuloConRelacionesSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    comprador = UserSerializer(read_only=True)
    categoria = CategoriaSerializer(read_only=True)
    estado = EstadoSerializer(read_only=True)
    condicion = CondicionSerializer(read_only=True)

    class Meta:
        model = Articulo
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    emisor = serializers.PrimaryKeyRelatedField(read_only=True)
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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['telefono', 'localidad', 'direccion', 'foto']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        # Podés agregar más campos personalizados si los tenés extendidos