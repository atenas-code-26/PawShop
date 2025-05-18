from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    AboutView,
    HomeView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    productos_por_categoria,
    agregar_al_carrito,
    ver_carrito,
    eliminar_del_carrito,
)

from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    # Productos
    path('productos/', ProductListView.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', ProductDetailView.as_view(), name='detalle_producto'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='crear_producto'),
    path('productos/editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='eliminar_producto'),

    # Navegación
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),

    # Autenticación
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', CreateView.as_view(
        template_name='signup.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login')
    ), name='signup'),

    # Categorías
    path('categoria/<int:categoria_id>/', productos_por_categoria, name='productos_por_categoria'),

    # Carrito
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/eliminar/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
]