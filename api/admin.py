from django.contrib import admin

from api.models import Cerveza, Comida, Titulo

class CervezaAdmin(admin.ModelAdmin):
    pass

class ComidaAdmin(admin.ModelAdmin):
    pass

class TituloAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cerveza, CervezaAdmin)

admin.site.register(Comida, ComidaAdmin)

admin.site.register(Titulo, TituloAdmin)
