from django.db import models


class Sucursal(models.Model):
    ciudad = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.ciudad


class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    stock = models.CharField(max_length=30)
    ciudadProducto = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
