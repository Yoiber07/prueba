from django.contrib import admin
from django.urls import path,include
from cliente.views import Home

urlpatterns = [
    path('cliente/', include(('cliente.urls','cliente'))),
    path('admin/', admin.site.urls),
    path('home/', Home, name="index"),
]
