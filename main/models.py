from django.db import models

# Create your models here.

class Contacto_Directo(models.Model):
    cedularuc = models.CharField(max_length=15)
    nombre = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    numero = models.CharField(max_length=15) 
    def __str__(self):              
        return self.cedularuc
    #class Meta:
        #ordering = ["nombre"]