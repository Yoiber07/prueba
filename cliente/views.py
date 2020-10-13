from django.shortcuts import render,redirect
from cliente.forms import ClienteForm
from django.contrib import messages
from .models import Clientes
def Home(request):
    return render(request,'inicio.html')

def crear_cliente(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            messages.error(request, "Ya existe un cliente con esta identificacion!!")
            return redirect("index")
    else:
        cliente_form = ClienteForm()
    return render(request, 'cliente/crear_cliente.html', {'form': cliente_form})

def listar_cliente(request):
    clientes = Clientes.objects.all()

    return render(request, 'cliente/listar_cliente.html',{'clientes':clientes})


def editar_cliente(request,id):
    cliente = Clientes.objects.get(docCliente=id)
    if request.method == 'GET':
        cliente_form = ClienteForm(instance=cliente)
    else:
        cliente_form = ClienteForm(request.POST,instance=cliente)
        if cliente_form.is_valid():
            cliente_form.save()
            redirect('index')
    return render(request, 'cliente/crear_cliente.html', {'form': cliente_form})