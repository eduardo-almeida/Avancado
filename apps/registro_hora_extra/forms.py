from django.forms import ModelForm
from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    def __int__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__int__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.fielter(empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']
