from django.urls import path
from .views import editar_usuario

urlpatterns = [
    path('editar-usuario/', editar_usuario, name='editar_usuario'),
]