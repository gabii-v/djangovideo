from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre


class Estado(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    visible = models.BooleanField(default=True)  # antes se llamaba "activo"

    def __str__(self):
        return self.descripcion


class Condicion(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion



class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articulos')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    condicion = models.ForeignKey(Condicion, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.titulo} - {self.usuario.username}"
    
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_enviados')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mensajes_recibidos')
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='mensajes')
    contenido = models.TextField()
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.emisor.username} a {self.receptor.username} sobre {self.articulo.titulo}"


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefono = models.CharField(max_length=20, blank=True)
    localidad = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=255, blank=True)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f"Perfil de {self.usuario.username}"