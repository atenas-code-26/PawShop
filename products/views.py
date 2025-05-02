from django.views.generic import ListView, DetailView,TemplateView
from .models import Producto, Categoria
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    carrito[str(producto_id)] = carrito.get(str(producto_id), 0) + 1
    request.session['carrito'] = carrito
    return redirect('lista_productos')

def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(id=producto_id)
        producto.cantidad = cantidad
        productos.append(producto)

    return render(request, 'products/carrito.html', {
        'productos': productos,
        'total': total
    })

def home_view(request):
    return render(request, 'products/home.html')

def productos_por_categoria(request, categoria_id):
    categoria = get_object_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria)
    return render(request, 'products/product_list.html', {'productos': productos, 'categoria':categoria})

class ProductoListView(ListView):
    model = Producto
    template_name = 'products/product_list.html'
    context_object_name = 'productos'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'products/product_detail.html'
    context_object_name = 'producto'

class AboutView(TemplateView):
    template_name = 'about.html'

class HomeView(TemplateView):
    template_name = 'home.html'