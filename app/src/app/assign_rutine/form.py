from django import forms
from app.assign_rutine.model import AssignRutine
from app.user.model import User
from app.trainer.model import Trainer
from app.rutine.model import Rutine

class AssignRutineForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'user'
        })
    )
    trainer = forms.ModelChoiceField(
        queryset=Trainer.objects.all(),
        label='Entrenador',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'trainer'
        })
    )
    rutine = forms.ModelChoiceField(
        queryset=Rutine.objects.all(),
        label='Rutina',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'rutine'
        })
    )

    class Meta:
        model = AssignRutine
        fields = ['user', 'trainer', 'rutine']

