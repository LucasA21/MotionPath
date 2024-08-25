from django import forms 
from app.exercise_type.model import ExerciseType

class ExerciseTypeForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del tipo de ejercicio',
        max_length=100,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del tipo de ejercicio',
            'maxlength':100,
        })
    )

    class Meta:
        model = ExerciseType
        fields = ['name']