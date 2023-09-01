from django.forms import ModelForm, TextInput, Select
from django import forms
from molienda.models import Atomizado, Barbotina, Granulometria


class DateInput(forms.DateField):
    input_type = 'date'


class FechaForm(forms.Form):
    date_field = forms.DateField(widget=DateInput)


class AtomizadoForm(ModelForm):
    class Meta:
        model = Atomizado
        fields = ['fecha', 'hora', 'codigo', 'nroSilo', 'humedad', 'observaciones', 'planta', 'barbotina',
                  'granulometria']
        widgets = {

            'nroSilo': forms.TextInput(attrs={'type': 'number'}),
        }

    def __init__(self, *args, **kwargs):
        super(AtomizadoForm, self).__init__(*args, **kwargs)
        self.fields['barbotina'] = forms.ModelChoiceField(queryset=Barbotina.objects.order_by('-fecha')[:10])
        self.fields['granulometria'] = forms.ModelChoiceField(queryset=Granulometria.objects.order_by('-fecha')[:10])
#        self.fields['barbotina'].queryset = Barbotina.objects.order_by('-fecha')[:15]
#        self.fields['granulometria'].queryset = Granulometria.objects.order_by('-fecha')[:15]


class BarbotinaForm(ModelForm):
    class Meta:
        model = Barbotina
        fields = ['fecha', 'hora', 'densidad', 'viscosidad', 'residuo', 'planta']
        widgets = {
            'densidad': TextInput(attrs={'type': 'decimal'}),
            'viscosidad':TextInput(attrs={'type': 'number'}),
            'residuo': TextInput(attrs={'type': 'decimal'}),

        }


class GranulometriaForm(ModelForm):
    class Meta:
        model = Granulometria
        fields = ['fecha', 'hora', 'malla500', 'malla425', 'malla300', 'malla180', 'fondo', 'planta']
        widgets = {
            'malla500': TextInput(attrs={'type': 'decimal'}),
            'malla425': TextInput(attrs={'type': 'decimal'}),
            'malla300': TextInput(attrs={'type': 'decimal'}),
            'malla180': TextInput(attrs={'type': 'decimal'}),
            'fondo': TextInput(attrs={'type': 'decimal'}),

        }
