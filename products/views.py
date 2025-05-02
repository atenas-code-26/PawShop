from django.views.generic import ListView, DetailView,TemplateView
from .models import Producto
from django.shortcuts import render

def home_view(request):
    return render(request, 'products/home.html')

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