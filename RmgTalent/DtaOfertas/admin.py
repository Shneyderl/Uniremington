from django.contrib import admin
from .models import Ofertas

# Register your models here.
class OfertasAdmin(admin.ModelAdmin):
    list_display = ('idOfer','idEmpOfer', 'titOfer', 'cargoOfer', 'descOfer', 'skillOfer', 'salOfer', 'contOfer','ubcOfer', 'catOfer', 'pubOfer', 'creaOfer', 'actuOfer')
    readonly_fields =('idOfer', 'creaOfer', 'actuOfer')
    search_fields=('idOfer', 'idEmpOfer', 'titOfer', 'cargoOfer')
    #ordering=('-creaAlu')
 
admin.site.register(Ofertas, OfertasAdmin)