from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

class DepartamentosCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentosCreate, self).form_valid(form)

class DepartamentosDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_funcionarios')

class DepartamentosUpdate(UpdateView):
    model = Departamento
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1])
        funcionario.save()
        return super(DepartamentosCreate, self).form_valid(form)