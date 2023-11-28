from django.contrib import admin
from .models import Categorias

# Register your models here.
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nomCat', 'desCat', 'pubCat', 'creaCat', 'actuCat')
    readonly_fields =('creaCat', 'actuCat')
    search_fields=('nomCat', 'desCat')
    #ordering=('-creaApp')
 
admin.site.register(Categorias, CategoriasAdmin)