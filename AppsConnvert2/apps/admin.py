from django.contrib import admin
from apps.models import Usuario

class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)

admin.site.register(Usuario, Usuarios)