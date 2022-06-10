import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Empresa

# Create your views here.

#Recibe los metodos HTTP
class EmpresaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #Obteniendo
    def get(self,request,id=0):
        if(id>0):
            empresas = list(Empresa.objects.filter(id=id).values())
            if len(empresas) > 0:
                empresa = empresas[0]
                datos = {'mensaje':"Exito", 'empresa': empresa}
            else:
                datos = {'mensaje':"No hay empresa para mostrar..."}
            return JsonResponse(datos)
        else:
            empresas = list(Empresa.objects.values())
            if len(empresas) > 0:
                datos = {'mensaje':"Exito", 'empresas': empresas}
            else:
                datos = {'mensaje':"No hay empresas para mostrar..."}
            return JsonResponse(datos)


    #Creando
    def post(self,request):
        #print(request.body)
        json_data = json.loads(request.body)
        #print(json_data)
        Empresa.objects.create(nombre=json_data['nombre'], direccion=json_data['direccion'], nit=json_data['nit'], telefono=json_data['telefono'])
        datos = {'mensaje': "Exito"}
        return JsonResponse(datos)


    #Actualizando
    def put(self,request,id):
        json_data = json.loads(request.body)
        empresas = list(Empresa.objects.filter(id=id).values())

        if len(empresas) > 0:
            empresa = Empresa.objects.get(id=id)
            empresa.nombre=json_data['nombre']
            empresa.direccion=json_data['direccion']
            empresa.nit=json_data['nit']
            empresa.telefono=json_data['telefono']
            empresa.save()
            datos = {'mensaje': "Exito"}
        else:
            datos = {'mensaje':"Empresa no encontrada..."}

        return JsonResponse(datos)

    #Eliminando
    def delete(self,request,id):
        empresas = list(Empresa.objects.filter(id=id).values())

        if len(empresas)>0:
            Empresa.objects.filter(id=id).delete()
            datos = {'mensaje': "Elinimacion Exitosa"}
        else:
            datos = {'mensaje':"Empresa no encontrada..."}
        
        return JsonResponse(datos)
