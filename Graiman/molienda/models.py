from django.db import models
from django.contrib.auth.models import User


class Planta(models.Model):
    nroPlanta = models.CharField(max_length=50)

    def __str__(self):
        return f'Planta  {self.nroPlanta}'


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)


class Barbotina(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    densidad = models.DecimalField(max_digits=10, decimal_places=2)
    viscosidad = models.IntegerField()
    residuo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    responsable = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.fecha} {self.hora} {self.planta}'


class Granulometria(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    malla500 = models.CharField(max_length=50)
    malla425 = models.CharField(max_length=50)
    malla300 = models.CharField(max_length=50)
    malla180 = models.CharField(max_length=50)
    fondo = models.CharField(max_length=50)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.fecha} {self.hora} {self.planta}'


class Atomizado(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    codigo = models.CharField(max_length=50)
    nroSilo = models.IntegerField()
    humedad = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    granulometria = models.ForeignKey(Granulometria, on_delete=models.CASCADE)
    barbotina = models.ForeignKey(Barbotina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.fecha} {self.hora} {self.nroSilo} {self.humedad} {self.observaciones} {self.granulometria} {self.barbotina} {self.planta} '
