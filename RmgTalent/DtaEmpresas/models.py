from django.db import models
from MainApp.models import TipoDoc

# Create your models here.
#        --------------       Tabla de Empresas        --------------        
class Empresas(models.Model):
    tipoDoc = models.ForeignKey(TipoDoc, on_delete=models.DO_NOTHING, verbose_name='Tipo de Documento', blank=True, null=True)
    idEmp = models.CharField(primary_key=True, max_length=12, unique=True, verbose_name='Número de NIT/RUT')
    nomEmp = models.CharField(max_length=200,verbose_name='Nombre Empresa')
    encarEmp = models.CharField(max_length=200,verbose_name='Nombre de representante')
    sectEmp = models.CharField(max_length=50,verbose_name='Sector')
    dirEmp = models.CharField(max_length=200,verbose_name='Dirección')    
    telEmp = models.CharField(max_length=10,null=True,blank=True,verbose_name='Tel. Contacto')
    mailEmp = models.CharField(max_length=100,null=True,blank=True,verbose_name='Correo Electronico')
    logoEmp = models.ImageField(default='null', verbose_name='Imagen', upload_to='Empresa', blank=True, null=True)
    pubEmp = models.BooleanField(default=False, verbose_name='Publicado?')
    creaEmp = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actuEmp = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
            
    def __str__(self):
        return str(self.idEmp)
