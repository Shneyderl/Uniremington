from django.contrib import admin
from .models import Alumnos

# Register your models here.
class AlumnosAdmin(admin.ModelAdmin):
    list_display = ('idAlu','nomAlu', 'apeAlu', 'carAlu', 'semAlu', 'pubAlu', 'creaAlu', 'actuAlu')
    readonly_fields =('creaAlu', 'actuAlu')
    search_fields=('idAlu', 'nomAlu', 'apeAlu', 'carAlu')
    #ordering=('-creaAlu')
 
admin.site.register(Alumnos, AlumnosAdmin)