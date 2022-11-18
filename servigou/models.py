from django.db import models
class Usuario(models.Model):
    documento = models.IntegerField(null=False, blank=False, primary_key=True, max_length=15)
    nombre = models.CharField(max_length=15, null=False, blank=False)
    apellido = models.CharField(max_length=10, null=False, blank=False)
    celular = models.IntegerField(null=False, blank=False, max_length=15)
    clave = models.IntegerField(null=False, blank=False, max_length=4)
    email = models.EmailField(null=False, blank=False,max_length=20)
    direccion = models.CharField(max_length=20, null=False, blank=False)
    

class Ruta(models.Model):
    valor_km = models.BigIntegerField(null=False,blank=False)
    km = models.IntegerField(null=False,blank=False)
    porcentaje_liquidacion = models.IntegerField(null=False,blank=False)
    incremento = models.DecimalField(null=True, blank=True)
    total_servicio = models.DecimalField(null=False,blank=False)
    total_liquidacion = models.DecimalField(null=False,blank=False)
    

#De uno a muchos
class Servicio(models.Model):
    servicio = models.IntegerField(null=False, blank=False, primary_key=True)
    fecha_hora = models.DateTimeField(null=False,blank=False)
    estado_servicio = models.CharField( max_length=10,null=False,blank=False)
    producto = models.models.CharField(max_length=200)
    documentos = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    rutas = models.ForeignKey(Ruta, on_delete=models.PROTECT )
    

#De uno a muchos
class Publicacion(models.Model):
    nombre_publicacion = models.CharField(null=False, blank=False, max_length=20 )
    tipo_archivo = models.CharField(null=False, blank=False, max_length=8)
    publicacion = models.ForeignKey(Usuario, on_delete=models.PROTECT )

#De muchos a muchos
class Rol(models.Model):
    nombre_rol = models.CharField(null=False, blank=False, max_length=12 )
    nivel_permiso = models.IntegerField(null=False, blank=False)
    usuario = models.ManyToManyField(Usuario, on_delete=models.PROTECT)