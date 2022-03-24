from django.db.models.base  import Model
from django.db.models.fields import BooleanField, CharField, DateField, EmailField, IntegerField

# Create your models here.

class Comentarios(Model):
    """Modelo que guarda los datos del articulos"""
    nombre = CharField(max_length=30)
    comentario = CharField(max_length=20)
    