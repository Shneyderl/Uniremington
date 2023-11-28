from django.contrib import admin
from .models import Empresas

# Register your models here.
class EmpresasAdmin(admin.ModelAdmin):
    list_display = ('tipoDoc', 'idEmp', 'nomEmp', 'encarEmp', 'sectEmp', 'dirEmp', 'telEmp', 'mailEmp', 'logoEmp', 'pubEmp', 'creaEmp', 'actuEmp')
    readonly_fields =('creaEmp', 'actuEmp')
    search_fields=('idEmp', 'nomEmp', 'encarEmp', 'sectEmp', 'dirEmp', 'telEmp', 'mailEmp')
    #ordering=('-creaApp')
 
admin.site.register(Empresas, EmpresasAdmin)