from django.forms import ModelForm, TextInput, Select
from django import forms
from molienda.models import Atomizado, Barbotina, Granulometria
from django.contrib.auth.models import User

class DateInput(forms.DateField):
    input_type = 'date'


class FechaForm(forms.Form):
    date_field = forms.DateField(widget=DateInput)


class AtomizadoForm(ModelForm):
    class Meta:
        model = Atomizado
        fields = ['fecha', 'hora', 'codigo', 'nroSilo', 'humedad', 'observaciones', 'planta', 'barbotina', 'granulometria']
        widgets = {
            'nroSilo': forms.TextInput(attrs={'type': 'number'}),
        }

    def __init__(self, *args, **kwargs):
        super(AtomizadoForm, self).__init__(*args, **kwargs)

# Obtenemos el último registro
        ultima_barbotina = Barbotina.objects.latest('fecha')
        ultima_granulometria = Granulometria.objects.latest('fecha')

# Agrega las opciones del último registro automáticamente en el formulario

        self.fields['barbotina'].queryset |= Barbotina.objects.filter(pk=ultima_barbotina.pk)
        self.fields['granulometria'].queryset |= Granulometria.objects.filter(pk=ultima_granulometria.pk)
# Limita las opciones a los últimos 10 registros
        self.fields['barbotina'].widget.choices = [(obj.pk, str(obj)) for obj in Barbotina.objects.order_by('-id')[:10]]
        self.fields['granulometria'].widget.choices = [(obj.pk, str(obj)) for obj in Granulometria.objects.order_by('-id')[:10]]



#    def __init__(self, *args, **kwargs):
#        super(AtomizadoForm, self).__init__(*args, **kwargs)
#        self.fields['barbotina'] = forms.ModelChoiceField(queryset=Barbotina.objects.order_by('-fecha')[:10])
#        self.fields['granulometria'] = forms.ModelChoiceField(queryset=Granulometria.objects.order_by('-fecha')[:10])
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

class FiltroAtomizadoForm(forms.Form):
    start_date = forms.DateField(label='Fecha de inicio', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Fecha de fin', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    planta_choices = [
        ('1', 'planta 1'),
        ('2', 'planta 2'),
        ('3', 'planta 3'),
    ]
    planta = forms.ChoiceField(label='Planta', required=False, choices=planta_choices)


class FiltroBarbotinaForm(forms.Form):
    start_date = forms.DateField(label='Fecha de inicio', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Fecha de fin', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    planta_choices = [
        ('1', 'planta 1'),
        ('2', 'planta 2'),
        ('3', 'planta 3'),
    ]
    planta = forms.ChoiceField(label='Planta', required=False, choices=planta_choices)
