from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    AboutView,
    HomeView,
    productos_por_categoria
)
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .views import agregar_al_carrito, ver_carrito


urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('categoria/<int:categoria_id>/', productos_por_categoria, name='productos_por_categoria'),
    path('agregar/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', ver_carrito, name='ver_carrito'),

    # Auth
    path('signup/', CreateView.as_view(
        template_name='signup.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login')
    ), name='signup'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]