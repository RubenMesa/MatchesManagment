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

    def get(self, request):
        verposicion=list(posiciones.objects.values())
        if len(verposicion)>0:
            datos={'message': "Exitoso", 'verposicion':verposicion}
        else:
            datos={'message': "No se encontraron posiciones..."}
        return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        posiciones.objects.create(nombre=jd['nombre'], descripcion=jd['descripcion'])
        datos={'message': "Exitoso"}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass