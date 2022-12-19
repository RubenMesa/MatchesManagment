from django.http.response import JsonResponse
from django.views import View
from .models import posiciones

# Create your views here.

class posicionesview(View):

    def get(self, request):
        verposicion=list(posiciones.objects.values())
        if len(verposicion)>0:
            datos={'message': "Exitoso", 'verposicion':verposicion}
        else:
            datos={'message': "No se encontraron posiciones..."}
        return JsonResponse(datos)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass