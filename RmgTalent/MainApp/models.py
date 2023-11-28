from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
#        --------------       Tabla de Tipo de Doc        --------------        
class TipoDoc(models.Model):
    nomDoc = models.CharField(primary_key=True, max_length=100, verbose_name= 'Tipo de documento')
    descDoc = models.CharField(max_length=150, null=True, blank=True, verbose_name='Descripcion')
    creaDoc = models.DateTimeField(auto_now_add=True,verbose_name='Creado')
    actuDoc = models.DateTimeField(auto_now=True, verbose_name='Actualizado')

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de documentos'

    def __str__(self):
        return str(self.nomDoc)

#        --------------       Tabla de Usuarios        --------------        
class Usuarios(models.Model):
    tipoDoc = models.ForeignKey(TipoDoc, on_delete=models.CASCADE, verbose_name='Tipo de Documento', blank=True, null=True)
    usuario = models.OneToOneField(User, verbose_name='Usuario', blank=True, null=True, on_delete=models.CASCADE)
    idUsr = models.CharField(max_length=12, unique=True, verbose_name='Cédula')
    dirUsr = models.CharField(max_length=200,verbose_name='Dirección')
    fnacUsr = models.DateField(null=True,blank=True,verbose_name='Fecha de Cumpleaños')
    telUsr = models.CharField(max_length=10,null=True,blank=True,verbose_name='Num. Celular')
    picUsr = models.ImageField(default='null', verbose_name='Imagen', upload_to='usuario', blank=True, null=True)
    pubUsr = models.BooleanField(default=False, verbose_name='Publicado?')
    creaUsr = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actuUsr = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
            
    def __str__(self):
        return str(self.idUsr)