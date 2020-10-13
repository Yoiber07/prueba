from django.contrib import admin
from cliente.forms import ClienteForm
from cliente.models import Clientes

admin.site.register(Clientes)
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ("fechaNacimiento",)
    form = ClienteForm

