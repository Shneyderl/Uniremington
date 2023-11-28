from django.db import models
#from django.contrib.auth.models import idOfer, idAlu
from DtaAlumnos.models import Alumnos
from DtaOfertas.models import Ofertas


# Create your models here.
#        --------------       Tabla de Ofertas        --------------        
class Aplica(models.Model):
    #idApp = models.CharField(auto_created=True, max_length=15, unique=True, verbose_name='Id') 
    idApp = models.AutoField(primary_key=True, verbose_name='Id')
    idOferApp = models.ForeignKey(Ofertas, on_delete=models.PROTECT, verbose_name='Id de Oferta', blank=True, null=True)
    idAluApp = models.ForeignKey(Alumnos, on_delete=models.PROTECT, verbose_name='Id de Alumno', blank=True, null=True)
    stsApp = models.CharField(max_length=200,verbose_name='Estatus de la aplicación')    
    creaApp = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actuApp = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Aplicacion'
        verbose_name_plural = 'Aplicaciones'
            
    def __str__(self):
        return str(self.idApp)