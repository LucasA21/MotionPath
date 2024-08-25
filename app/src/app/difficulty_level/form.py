from typing import Any
from django import forms
from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del nivel de dificultad',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del nivel de dificultad',
            'maxlength':100,
        })  
    )

    class Meta:
        model = DifficultyLevel
        fields = ['name']
        