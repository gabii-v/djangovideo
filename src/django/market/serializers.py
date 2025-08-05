# market/serializers.py

from rest_framework import serializers
from .models import Categoria, Estado, Condicion, Articulo, Mensaje, FotoArticulo
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

class FotoArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = FotoArticulo
        fields = ['id', 'imagen']

class ArticuloSerializer(serializers.ModelSerializer):
    usuario_username = serializers.ReadOnlyField(source='usuario.username')
    categoria_nombre = serializers.ReadOnlyField(source='categoria.nombre')
    estado_descripcion = serializers.ReadOnlyField(source='estado.descripcion')
    condicion_descripcion = serializers.ReadOnlyField(source='condicion.descripcion')
    fotos = FotoArticuloSerializer(many=True, read_only=True)  # esto usa el related_name 'fotos'

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
            'fotos',
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
    fotos = FotoArticuloSerializer(many=True, read_only=True)

    class Meta:
        model = Articulo
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    emisor = serializers.PrimaryKeyRelatedField(read_only=True)
    receptor = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    mensaje_padre = serializers.PrimaryKeyRelatedField(
        queryset=Mensaje.objects.all(),
        required=False,
        allow_null=True
    )

    emisor_username = serializers.ReadOnlyField(source='emisor.username')
    receptor_username = serializers.ReadOnlyField(source='receptor.username')
    articulo_titulo = serializers.ReadOnlyField(source='articulo.titulo')
    respuestas = serializers.SerializerMethodField()

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
            'mensaje_padre',     # <--- Ya editable
            'respuestas',
        ]

    def get_respuestas(self, obj):
        respuestas = Mensaje.objects.filter(mensaje_padre=obj).order_by('fecha_envio')
        return MensajeSerializer(respuestas, many=True).data


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

# class UsuarioSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'first_name', 'last_name']
#        # Podés agregar más campos personalizados si los tenés extendidos

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': False, 'allow_blank': True},
            'last_name': {'required': False, 'allow_blank': True},
        }