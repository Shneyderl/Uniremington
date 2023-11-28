from django.db import models

# Create your models here.
#        --------------       Tabla de Alumnos        --------------       
class Alumnos(models.Model):
    idAlu = models.CharField(primary_key=True, max_length=12, unique=True, verbose_name='Num. documento')
    nomAlu = models.CharField(max_length=200,verbose_name='Nombres')
    apeAlu = models.CharField(max_length=200,verbose_name='Apellidos')        
    carAlu = models.CharField(max_length=200,verbose_name='Carrera')
    semAlu = models.CharField(max_length=10,verbose_name='Semestre')
    pubAlu = models.BooleanField(default=False, verbose_name='Publicado?')
    creaAlu = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    actuAlu = models.DateTimeField(auto_now=True, verbose_name='Actualizado')
    
    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
            
    def __str__(self):
        return str(self.idAlu)
    
    # def calcular_edad(self):
    #     return date.today().year - self.fnacAlu.year
