from django.db import models

# Create your models here.
#        --------------       Tabla de Categorias        --------------        
class Categorias(models.Model):
    #idCat = models.CharField(primary_key=True, auto_created=True, max_length=15, unique=True, verbose_name='Id')    
    idCat = models.AutoField(primary_key=True, verbose_name='Id')
    nomCat = models.CharField(max_length=20,null=True,blank=True,verbose_name='Nombre')
    desCat = models.CharField(max_length=200,null=True,blank=True,verbose_name='Descripción')
    pubCat = models.BooleanField(default=False, verbose_name='Publicado?')
    creaCat = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actuCat = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
            
    def __str__(self):
        return str(self.idCat)