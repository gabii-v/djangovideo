#from django.contrib.auth.models import AbstractUser
#from django.db import models
#
#class UsuarioPersonalizado(AbstractUser):
#    nombre_completo = models.CharField(max_length=100, blank=True, null=True)
#    telefono = models.CharField(max_length=20, blank=True, null=True)
#    localidad = models.CharField(max_length=100, blank=True, null=True)
#    direccion = models.TextField(blank=True, null=True)
#    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
#
#    def __str__(self):
#        return self.username
