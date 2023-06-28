from django.db import models

# Create your models here.
class Comuna(models.Model):
    idcomuna = models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Genero(models.Model):
    idgenero = models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    comentario = models.CharField(max_length=100)

class Marca(models.Model):
    idmarca = models.AutoField(primary_key=True)
    descripcion= models.CharField(max_length=50)
    estado = models.IntegerField()

    def __str__(self):
        return self.descripcion

class Celular(models.Model):
    idcelu = models.AutoField(primary_key=True)
    modelo = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    file = models.ImageField(upload_to="img/")
    precio = models.FloatField()
    stock = models.IntegerField()
    comentario = models.CharField(max_length=100)
    
    def __str__(self):
        return self.modelo
