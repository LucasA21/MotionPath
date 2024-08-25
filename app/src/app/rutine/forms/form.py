from django import forms

from app.difficulty_level.model import DifficultyLevel
from app.rutine_type.model import RutineType
from app.rutine.model import Rutine

class RutineForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre de la Rutina',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Ingrese el nombre de la rutina',
            'maxlength': 60
        })
    )
    difficulty_level = forms.ModelChoiceField(
        queryset=DifficultyLevel.objects.all(),
        label='Nivel de Dificultad',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'difficulty_level'
        })
    )
    rutine_type = forms.ModelMultipleChoiceField(
        queryset=RutineType.objects.all(),
        label='Tipos de Rutina',
        required=True,
        widget=forms.SelectMultiple(attrs={
            'class': 'choices form-select form-control-lg multiple-remove',
            'id': 'rutine_type'
        })
    )

    class Meta:
        model = Rutine
        fields = ['name', 'difficulty_level', 'rutine_type']

    def clean(self):
        cleaned_data = super().clean()
        difficulty_level = cleaned_data.get('difficulty_level')
        if difficulty_level is None:
            raise forms.ValidationError('Debe especificar un nivel de dificultad para la rutina.')
        return cleaned_data
