from django.views.generic import ListView, DetailView,TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from .models import Producto, Categoria
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductoForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

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


def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    producto_id_str = str(producto_id)
    if producto_id_str in carrito:
        if carrito[producto_id_str] > 1:
            carrito[producto_id_str] -= 1
        else:
            del carrito[producto_id_str]
        request.session['carrito'] = carrito
    return redirect('ver_carrito')


class ProductListView(ListView):
    model = Producto
    template_name = 'products/product_list.html'
    context_object_name = 'productos'

class ProductDetailView(DetailView):
    model = Producto
    template_name = 'products/product_detail.html'
    context_object_name = 'producto'

class AboutView(TemplateView):
    template_name = 'about.html'

class HomeView(TemplateView):
    template_name = 'home.html'


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'products/producto_form.html'
    success_url = reverse_lazy('lista_productos')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'products/producto_confirm_delete.html'
    success_url = reverse_lazy('lista_productos')

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'products/producto_form.html'
    success_url = reverse_lazy('lista_productos')


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'products/crear_producto.html', {'form': form})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'products/editar_producto.html', {'form': form, 'producto': producto})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'products/eliminar_producto.html', {'producto': producto})