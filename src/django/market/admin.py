from django.contrib import admin
from .models import Categoria, Estado, Condicion, Articulo, Mensaje, FotoArticulo

admin.site.register(Categoria)
admin.site.register(Estado)
admin.site.register(Condicion)
admin.site.register(Articulo)
admin.site.register(Mensaje)
admin.site.register(FotoArticulo)
