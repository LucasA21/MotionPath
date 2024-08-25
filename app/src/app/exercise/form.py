from django import forms

from app.difficulty_level.model import DifficultyLevel
from app.exercise_type.model import ExerciseType
from app.user.model import User
from app.exercise.model import Exercise

class ExerciseForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del ejercicio',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder': 'Ingrese el nombre del ejercicio',
            'maxlength': 60,
        })
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'user'
            })
    )
    difficulty_level = forms.ModelChoiceField(
        queryset=DifficultyLevel.objects.all(),
        label='Nivel de Dificultad',
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'difficulty_level'
            })
    )
    exercise_type = forms.ModelMultipleChoiceField(
        queryset=ExerciseType.objects.all(),
        label='Tipos de Ejercicio',
        widget=forms.SelectMultiple(attrs={
            'class': 'choices form-select form-control-lg multiple-remove',
            'id': 'exercise_type'
        })
    )

    class Meta:
        model = Exercise
        fields = ['name', 'user', 'difficulty_level', 'exercise_type']

    def clean(self):
        cleaned_data = super().clean()
        difficulty_level = cleaned_data.get('difficulty_level')
        if difficulty_level is None:
            raise forms.ValidationError('Debe especificar un nivel de dificultad')
        return cleaned_data