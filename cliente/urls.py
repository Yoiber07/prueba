from django.urls import path
from cliente  import views


urlpatterns = [
    path('crear-cliente/', views.crear_cliente, name="crear"),
    path('listar-cliente/', views.listar_cliente, name="listar"),
    path('editar-cliente/<int:id>/', views.editar_cliente, name="editar"),
    ]