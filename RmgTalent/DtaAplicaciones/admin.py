from django.contrib import admin
from .models import Aplica

# Register your models here.
class AplicaAdmin(admin.ModelAdmin):
    list_display = ('idApp', 'idOferApp', 'idAluApp', 'stsApp', 'creaApp', 'actuApp')
    readonly_fields =('idApp', 'creaApp', 'actuApp')
    search_fields=('idApp', 'idOferApp', 'idAluApp', 'stsApp')
    #ordering=('-creaApp')
 
admin.site.register(Aplica, AplicaAdmin)
