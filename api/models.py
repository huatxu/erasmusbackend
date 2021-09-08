from django.db import models

class Cerveza(models.Model):
    nombre = models.CharField(max_length=255)
    estilo = models.CharField(max_length=255)
    pais = models.CharField(max_length=255)
    pais_ingles = models.CharField(max_length=255)
    alcohol	 = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    amargor	 = models.CharField(max_length=255)
    descripcion = models.CharField(null=True, blank=True, max_length=1024)
    descripcion_ingles = models.CharField(null=True, blank=True, max_length=1024)
    disponible = models.BooleanField(max_length=255)
    imagen = models.URLField(null=True, blank=True)
    artesanal = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    recomendada	 = models.BooleanField()
    formato	 = models.CharField(null=True, blank=True, max_length=255)
    precio = models.DecimalField(decimal_places=2, max_digits=12)
    formato_2 = models.CharField(null=True, blank=True, max_length=255)
    precio_2 = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=12)
    formato_3 = models.CharField(null=True, blank=True, max_length=255)
    precio_3 = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=12)
    sin_gluten = models.BooleanField()
    aparece	= models.BooleanField()
    barril = models.BooleanField()

class TipoComida(models.Model):
    nombre = models.CharField(max_length=255)
    nombre_ingles = models.CharField(max_length=255)
    orden = models.IntegerField(default=0)
    aparece = models.BooleanField(default=True)
    class Meta:
        verbose_name_plural = "Familias de Comida"
        verbose_name = "Familia de comida"

    def __str__(self):
        return self.nombre

class Comida(models.Model):
    orden = models.IntegerField(default=0)
    nombre = models.CharField(max_length=255)
    nombre_ingles = models.CharField(max_length=255)
    descripcion = models.CharField(null=True, blank=True, max_length=1024)
    descripcion_ingles = models.CharField(null=True, blank=True, max_length=1024)
    tipo = models.ForeignKey(TipoComida, on_delete=models.CASCADE)
    precio = models.DecimalField(decimal_places=2, max_digits=12)
    precio_2 = models.DecimalField(decimal_places=2, max_digits=12)
    altramuces = models.BooleanField()
    apio = models.BooleanField()
    cacahuete = models.BooleanField()
    crustaceo = models.BooleanField()
    gluten = models.BooleanField()
    huevo = models.BooleanField()
    lacteos = models.BooleanField()
    moluscos = models.BooleanField()
    mostaza = models.BooleanField()
    nueces = models.BooleanField()
    pescado = models.BooleanField()
    sesamo = models.BooleanField()
    soja = models.BooleanField()
    sulfitos = models.BooleanField()
    disponible = models.BooleanField()

class Titulo(models.Model):
    titulo_1 = models.CharField(null=True, blank=True, max_length=1024)
    titulo_1_ingles = models.CharField(null=True, blank=True, max_length=1024)
    titulo_2 = models.CharField(null=True, blank=True, max_length=1024)
    titulo_2_ingles = models.CharField(null=True, blank=True, max_length=1024)