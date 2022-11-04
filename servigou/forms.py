from django.forms import ModelForm,TextInput
from .models import Ruta

class RutaForm(ModelForm):
    class Meta:
        model = Ruta
        fields = '__all__'
        widgets = {
            'valor_km': TextInput(attrs={'class':'form-control'}),
            'km': TextInput(attrs={'class':'form-control'}),
            'porcentaje': TextInput(attrs={'class':'form-control'}) ,
            'total': TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'valor_km': 'Valor del kilometro',
            'km': 'Kilometros del recorrido',
            'porcentaje': 'Porcenta de liquidacion' ,
            'total': 'Total del servicio',
        }
