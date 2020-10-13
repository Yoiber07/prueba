from django import forms
from cliente.models import Clientes

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ('docCliente','nombres','primerApellido','segundoApellido','email','celular','fechaNacimiento',)