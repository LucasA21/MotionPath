from django import forms
from app.user.model import User  
from app.trainer.model import Trainer 

class TrainerForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'user'
        })
    )

    is_verify = forms.BooleanField(
        label='Verificado',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'is_verify'
        })
    )

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        label='Usuarios',
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'choices form-select form-control-lg multiple-remove',
            'id': 'users'
        })
    )


    class Meta:
        model = Trainer
        fields = ['user', 'is_verify', 'rate', 'users']

    class Meta:
        model = Trainer
        fields = ['user', 'is_verify']
