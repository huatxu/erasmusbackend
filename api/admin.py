from django.contrib import admin

from api.models import Cerveza, Comida, Titulo

class CervezaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre',)
class ComidaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('nombre',)

class TituloAdmin(admin.ModelAdmin):
    list_display = ('titulo_1',)


admin.site.register(Cerveza, CervezaAdmin)

admin.site.register(Comida, ComidaAdmin)

admin.site.register(Titulo, TituloAdmin)
