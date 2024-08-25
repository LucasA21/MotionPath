from django import forms
from app.rutine.model import Rutine

class PickRutineForm(forms.Form):
    rutine = forms.ModelChoiceField(
        queryset=Rutine.objects.all(),  
        label="Selecciona una Rutina",
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'rutine'
        })
    )

    class Meta:
        model = Rutine
        fields = ['rutine']
