#from django.shortcuts import render
import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
from .models import Musician, Album
from .serializers import PersonaSerializer, PersonSerializer
from .models import Person


# Create your views here.
def nuevoHello(request): 
    return HttpResponse("Hola mundo!!!")

def bye(request): 
    return HttpResponse("Hasta luego!!!")

def edad(request, anios, futuro):
    incremento = futuro - date.today().year
    cumplira = anios + incremento

    mensaje = "En el año %d cumpliras %d años"%(futuro, cumplira)

    return HttpResponse(mensaje)

def primer_plantilla(request):
    plantilla = """
    <html>
        <body>
            <h2>
                Hola {{ nombre }}! esta es mi primer plantilla!
            </h2>
        </body>
    </html>
    """
    
    tpl = Template(plantilla)

    ctx = Context({
        'nombre': 'Gabriel Matias'
    })

    mensaje = tpl.render(ctx)

    return HttpResponse(mensaje)

def segunda_plantilla(request):
    
    tpl = get_template("segunda_plantilla.html")

    mensaje = tpl.render({
        'nombre': 'Gabriel Matias',
        'fecha_actual': date.today()
    })

    return HttpResponse(mensaje)

def tercer_plantilla(request):
    
    return render(request, "tercer_plantilla.html", {
        'nombre': 'Pedro Gómez',
        'fecha_actual': date.today()
    })

class Empleado(object):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

def cuarta_plantilla(request):

    empleado = Empleado ('Juan', 'Gómez')

    laborables = ['Lunes', 'Martes', 'Miércoles', 'Jueves']
    
    return render(request, "cuarta_plantilla.html", {
        'mi_empleado': empleado,
        'fecha_actual': date.today(),
        'dias_laborables': laborables
    }) 

def crear_musico(request, nombre, apellido, instrumento):
    per=Musician(first_name=nombre, last_name=apellido, instrument=instrumento )
    per.save()
    mensaje = "Se creó el músico %s %s con id %d"%(per.first_name, per.last_name, per.id)

    return HttpResponse(mensaje)

def crear_albun(request, nombre, estrellas, artista_id):
    art=Musician.objects.get(id=artista_id)
    albun=Album(name=nombre, release_date=date.today(), num_stars=estrellas, artist=art)
    albun.save()
    mensaje = "Se creó el Albun %s del Artista %s con id %d"%(albun.name, art.last_name, albun.id)

    return HttpResponse(mensaje)

@csrf_exempt
def first_api(request):
    if request.method == 'GET': 
        respuesta = {
            'nombre': 'Juan',
            'apellido': 'Perez',
            'edad': 25
        }
        return JsonResponse(respuesta)
    elif request.method == 'POST':
        datos = json.loads(request.body)
        nombre = datos['nombre']
        apellido = datos['apellido']
        edad = datos['edad']
        respuesta = {
            'nombre2': nombre,
            'apellido2': apellido,
            'edad2': edad
        }
        return JsonResponse(respuesta)
    return None

@csrf_exempt
def serialv1(request):
    if request.method == 'POST':
        datos = json.loads(request.body)
        serializador = PersonaSerializer(data=datos)
        if serializador.is_valid():
            return JsonResponse(serializador.validated_data, status=201)
        else:
            return JsonResponse(serializador.errors, status=400)
                    
    return None

@csrf_exempt
def person_list(request):

    if request.method == 'GET':
        personas = Person.objects.all()
        serializer = PersonSerializer(personas, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'POST':
        datos = json.loads(request.body)
        serializer = PersonSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.data, status=400)
    
    return None


@csrf_exempt
def person_detail(request, pk):

    if request.method == 'GET':
        persona = Person.objects.get(pk=pk)
        serializer = PersonSerializer(persona)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'PUT':
        datos = json.loads(request.body)
        persona = Person.objects.get(pk=pk)
        serializer = PersonSerializer(persona, data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.data, status=400)
        
    if request.method == 'DELETE':
        persona = Person.objects.get(pk=pk)
        persona.delete()
        return HttpResponse(status=204)
    
    return None