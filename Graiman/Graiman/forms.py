from django.forms import ModelForm, TextInput

from molienda.models import Atomizado, Barbotina, Granulometria


class AtomizadoForm(ModelForm):
    class Meta:
        model = Atomizado
        fields = '__all__'
        widgets = {
            'Planta': TextInput(attrs={'type': 'number'}),
            'NroSilo': TextInput(attrs={'type': 'number'})
        }

class BarbotinaForm(ModelForm):
    class Meta:
        model = Barbotina
        fields = '__all__'
        widgets = {
            'Densidad': TextInput(attrs={'type': 'decimal'}),
            'Viscosidad': TextInput(attrs={'type': 'number'}),
            'Residuo': TextInput(attrs={'type': 'decimal'})
        }

class GranulometriaForm(ModelForm):
    class Meta:
        model = Granulometria
        fields = '__all__'
        widgets = {
            'Malla500': TextInput(attrs={'type': 'decimal'}),
            'Malla425': TextInput(attrs={'type': 'decimal'}),
            'Malla300': TextInput(attrs={'type': 'decimal'}),
            'Malla180': TextInput(attrs={'type': 'decimal'}),
            'Fondo': TextInput(attrs={'type': 'decimal'})
        }