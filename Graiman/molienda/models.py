from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.nombre} {self.apellido}'


class Planta(models.Model):
    nroPlanta = models.CharField(max_length=50)

    def __str__(self):
        return f'Planta  {self.nroPlanta}'


class Barbotina(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    densidad = models.DecimalField(max_digits=10, decimal_places=2)
    viscosidad = models.IntegerField()
    residuo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f' {self.id}: {self.densidad} {self.viscosidad} {self.residuo}'


class Granulometria(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    malla500 = models.CharField(max_length=50)
    malla425 = models.CharField(max_length=50)
    malla300 = models.CharField(max_length=50)
    malla180 = models.CharField(max_length=50)
    fondo = models.CharField(max_length=50)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f' {self.id}: {self.malla500} {self.malla425} {self.malla300} {self.malla180} {self.fondo}'


class Atomizado(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    codigo = models.CharField(max_length=50)
    nroSilo = models.IntegerField()
    humedad = models.CharField(max_length=50)
    observaciones = models.CharField(max_length=500, null=True, blank=True)
    planta = models.ForeignKey(Planta, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)
    granulometria = models.ForeignKey(Granulometria, on_delete=models.CASCADE)
    barbotina = models.ForeignKey(Barbotina, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id}: {self.fecha} {self.hora} {self.nroSilo} {self.humedad} {self.observaciones} {self.granulometria} {self.barbotina} {self.planta} '
