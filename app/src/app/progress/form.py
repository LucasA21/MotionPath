from django import forms
from app.progress.model import Progress
from app.user.model import User
from app.exercise.model import Exercise

class ProgressForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'user'
        })
    )

    exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        label='Ejercicios',
        required=True,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select form-control-lg',
            'id': 'exercises'
        })
    )

    weight = forms.FloatField(
        label='Peso',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'weight'
        })
    )

    repetitions = forms.IntegerField(
        label='Repeticiones',
        required=True,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'id': 'repetitions'
        })
    )

    class Meta:
        model = Progress
        fields = ['user', 'exercises', 'weight', 'repetitions']
