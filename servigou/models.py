from django.db import models

# Create your models here.
class Ruta(models.Model):
    valor_km : models.BigIntegerField(null=False,blank=False)
    km = models.IntegerField(null=False,blank=False)
    porcentaje = models.IntegerField(default=25)
    total = models.BigIntegerField(null=False,blank=False)

#De uno a muchos
class Servicio(models.Model):
    servicio = models.ForeignKey(Ruta, on_delete=models.PROTECT)

