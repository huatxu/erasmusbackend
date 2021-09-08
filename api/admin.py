from django.contrib import admin

from api.models import Cerveza, Comida, Titulo, TipoComida

class CervezaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'tipo', 'disponible', 'barril', 'precio', 'precio_2', 'precio_3')
    search_fields = ('nombre',)
    list_filter = ('tipo','disponible','barril')
    list_editable = ('disponible',)

class ComidaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'tipo', 'disponible', 'precio', 'precio_2', 'orden')
    search_fields = ('nombre',)
    list_filter = ('tipo','disponible',)
    list_editable = ('disponible','orden')

class TituloAdmin(admin.ModelAdmin):
    list_display = ('titulo_1',)


class TipoComidaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_ingles', 'orden', 'aparece')
    list_editable = ('orden', 'aparece')


admin.site.register(TipoComida, TipoComidaAdmin)

admin.site.register(Cerveza, CervezaAdmin)

admin.site.register(Comida, ComidaAdmin)

admin.site.register(Titulo, TituloAdmin)
