from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='productos/')
    fecha_publicacion = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre