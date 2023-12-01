from django.db import models
#from django.contrib.auth.models import idEmp, nomCat
from DtaEmpresas.models import Empresas
from DtaCategorias.models import Categorias


# Create your models here.
#        --------------       Tabla de Ofertas        --------------        
class Ofertas(models.Model):
    #idOfer = models.CharField(primary_key=True, max_length=15, auto_created=True, unique=True, verbose_name='Id')    
    idOfer = models.AutoField(primary_key=True, verbose_name='Id')
    idEmpOfer = models.ForeignKey(Empresas, on_delete=models.PROTECT, verbose_name='NIT Empresa', blank=True, null=True)
    titOfer = models.CharField(max_length=200,verbose_name='Titulo Oferta')
    cargoOfer = models.CharField(max_length=100,verbose_name='Cargo')
    descOfer = models.TextField(max_length=500,null=True,blank=True,verbose_name='Descripción Oferta')
    skillOfer = models.TextField(max_length=500,null=True, blank=True, verbose_name='Requerimientos')
    salOfer = models.CharField(max_length=10,null=True,blank=True,verbose_name='Salario')
    contOfer = models.CharField(max_length=20,null=True,blank=True,verbose_name='Contrato')
    ubcOfer = models.CharField(max_length=20,null=True,blank=True,verbose_name='Ubicación')
    catOfer = models.ForeignKey(Categorias, on_delete=models.PROTECT, verbose_name='Categoria', blank=True, null=True)
    pubOfer = models.BooleanField(default=False, verbose_name='Publicado?')
    creaOfer = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actuOfer = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Oferta'
        verbose_name_plural = 'Ofertas'
            
    def __str__(self):
        return str(self.idOfer)
