from django.contrib import admin
from .models import TipoDoc
from .models import Usuarios

# Register your models here.
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nomDoc', 'creaDoc', 'actuDoc')
    #readonly_fields =('creaDoc', 'actuDoc')
    search_fields=('nomDoc',)
    #ordering=('-creaDoc')

class UserAdmin(admin.ModelAdmin):
    list_display = ('usuario','idUsr', 'dirUsr', 'fnacUsr', 'telUsr', 'picUsr', 'creaUsr', 'actuUsr')
    readonly_fields =('creaUsr', 'actuUsr')
    search_fields=('idUsr', 'dirUsr', 'telUsr')
    #ordering=('-creaUsr')
 
admin.site.register(TipoDoc, TipoDocumentoAdmin)
admin.site.register(Usuarios, UserAdmin)