from django.urls import path
from .views import EmpresaCreate

urlpatterns = [
    path('criarEmpresa', EmpresaCreate.as_view(), name='criarEmpresa'),
]