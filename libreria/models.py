from django.db import models

# Create your models here.

class Libro(models.Model):

    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50, unique=True)
    imagen = models.ImageField(upload_to='libros', null=True, blank=True)
    descripcion = models.TextField()

