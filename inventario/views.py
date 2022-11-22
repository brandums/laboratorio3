from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import Categoria, Producto, Restaurante, Usuario
from .forms import ProductoForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .serializers import CategoriaSerializer, RestauranteSerializer, UsuarioSerializer



def index(request):
    return HttpResponse("hello world")

# Create your views here.
def contacto(request, nombre):
    return HttpResponse("hello world")

def categorias(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre:
        q = Categoria(nombre=post_nombre)
        q.save()
    filtro_nombre = request.GET.get("nombre")
    if filtro_nombre:
        categorias = Categoria.objects.filter(nombre__contains = filtro_nombre)
    else:
        categorias = Categoria.objects.all()
    return render(request, "categorias.html", {"categorias": categorias})


def productFormView(request):
    form = ProductoForm()
    producto = None
    id_producto = request.GET.get('id')
    
    if id_producto:
        producto = get_object_or_404(Producto, id= id_producto)
        # producto = Producto.objects.get(id= id_producto)
        form = ProductoForm(instance=producto)
    
    if request.method == 'POST':
        if producto:
            form = ProductoForm(request.POST, instance=producto)
        else: 
            form = ProductoForm(request.POST) 
    
    if form.is_valid():
        form.save()
    return render(request, "form_producto.html", {"form": form})


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


@api_view(["GET"])
def categoria_contador(request):
    """
    Cantidad de categorias registradas
    """
    try:
        cantidad = Categoria.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
        safe= False,
        status = 200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def usuario_contador(request):
    """
    Cantidad de usuarios registradas
    """
    try:
        usuarios = Usuario.objects.count()
        return JsonResponse(
            {
                "cantidad": usuarios
            },
        safe= False,
        status = 200,
        )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)