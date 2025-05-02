from django.urls import path
from .views import (
    ProductoListView,
    ProductoDetailView,
    AboutView,
    HomeView
)
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='lista_productos'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='detalle_producto'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
    path('logout/',LogoutView.as_view(), name='logout'),

    # Auth
    path('signup/', CreateView.as_view(
        template_name='signup.html',
        form_class=UserCreationForm,
        success_url=reverse_lazy('login')
    ), name='signup'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]