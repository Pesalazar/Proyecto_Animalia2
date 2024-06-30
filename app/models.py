from django.db import models

# Create your models here.


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=10)
    nombre_producto = models.CharField(max_length=20)
    fecha_vencimiento = models.DateField(blank=False, null=False)
    cantidad_producto = models.CharField(max_length=45)
    Marca =  models.CharField(max_length=45)
    activo = models.IntegerField()

    def __str__(self):
        return str (self.nombre_producto)