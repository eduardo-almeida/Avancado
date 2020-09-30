from django.urls import path
from .views import DepartamentosList, DepartamentosCreate, DepartamentosDelete, DepartamentosUpdate



urlpatterns = [
    path('list', DepartamentosList.as_view(), name='list_funcionarios'),
    path('novo/', DepartamentosCreate.as_view(), name='create_departamento'),
    path('delete/', DepartamentosDelete.as_view(), name='delete_departamento'),
    path('update/', DepartamentosUpdate.as_view(), name='update_departamento'),
]