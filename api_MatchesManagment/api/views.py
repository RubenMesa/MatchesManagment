from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import posiciones
import json

# Create your views here.

class posicionesview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            verposicion= list(posiciones.objects.filter(id=id).values())
            if len(verposicion)>0:
                posi= verposicion[0]
                datos={'message': "Exitoso", 'verposicion':posi}
            else:
                datos={'message': "No se encontró la posicion..."}
            return JsonResponse(datos)
        else:
            verposicion=list(posiciones.objects.values())
            if len(verposicion)>0:
                datos={'message': "Exitoso", 'verposicion':verposicion}
            else:
                datos={'message': "No se encontraron posiciones..."}
            return JsonResponse(datos)

    def post(self, request):
        jd=json.loads(request.body)
        posiciones.objects.create(nombre=jd['nombre'], descripcion=jd['descripcion'])
        datos={'message': "Agregada exitosamente"}
        return JsonResponse(datos)

    def put(self, request,id):
        jd=json.loads(request.body)
        verposicion= list(posiciones.objects.filter(id=id).values())
        if len(verposicion)>0:
            posi=posiciones.objects.get(id=id)
            posi.nombre=jd['nombre']
            posi.descripcion=jd['descripcion']
            posi.save()
            datos={'message': "Modificación Completada."}
        else:
            datos={'message': "No se encontró la posicion..."}
        return JsonResponse(datos)


    def delete(self, request,id):
        verposicion= list(posiciones.objects.filter(id=id).values())
        if len(verposicion)>0:
            posiciones.objects.filter(id=id).delete()
            datos={'message': "Se eliminó de forma exitosa"}
        else:
            datos={'message': "No se encontró la posicion..."}
        return JsonResponse(datos)
        