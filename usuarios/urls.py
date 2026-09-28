from .views import lista_usuarios ,detalle_usuario
from django.urls import path



urlpatterns = [
    path('usuarios/', lista_usuarios),
    path('usuarios/<int:id>/', detalle_usuario),
]