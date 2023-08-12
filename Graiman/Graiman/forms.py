from django.forms import ModelForm, TextInput
from django import forms
from molienda.models import Atomizado, Barbotina, Granulometria

class DateInput(forms.DateField):
    input_type = 'date'
class FechaForm(forms.Form):
    date_field = forms.DateField(widget=DateInput)


class AtomizadoForm(ModelForm):
    class Meta:
        model = Atomizado
        fields = ['fecha', 'hora', 'codigo', 'nroSilo', 'humedad', 'observaciones', 'planta', 'barbotina', 'granulometria']
        widgets = {
            'Fecha': TextInput(attrs={'date_field': DateInput}),
            'Planta': TextInput(attrs={'type': 'number'}),
            'NroSilo': TextInput(attrs={'type': 'number'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        registros_barbotina = Barbotina.objects.order_by('-fecha')[:5]
        registros_granulometria = Granulometria.objects.order_by('-fecha')[:5]

        self.fields['barbotina'].queryset = registros_barbotina
        self.fields['granulometria'].queryset = registros_granulometria


class BarbotinaForm(ModelForm):
    class Meta:
        model = Barbotina
        fields = ['fecha', 'hora', 'densidad', 'viscosidad', 'residuo', 'planta']
        widgets = {
            'Densidad': TextInput(attrs={'type': 'decimal'}),
            'Viscosidad':TextInput(attrs={'type': 'number'}),
            'Residuo': TextInput(attrs={'type': 'decimal'}),
            'Fecha': TextInput(attrs={'date_field': DateInput}),
            'usuario': TextInput(attrs={'type': 'varChar'})
        }


class GranulometriaForm(ModelForm):
    class Meta:
        model = Granulometria
        fields = ['fecha', 'hora', 'malla500', 'malla425', 'malla300', 'malla180', 'fondo', 'planta']
        widgets = {
            'Malla500': TextInput(attrs={'type': 'decimal'}),
            'Malla425': TextInput(attrs={'type': 'decimal'}),
            'Malla300': TextInput(attrs={'type': 'decimal'}),
            'Malla180': TextInput(attrs={'type': 'decimal'}),
            'Fondo': TextInput(attrs={'type': 'decimal'}),
            'Fecha': TextInput(attrs={'date_field': DateInput}),
        }
