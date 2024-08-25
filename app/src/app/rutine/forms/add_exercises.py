from django import forms

from app.rutine.model import Rutine
from app.exercise.model import Exercise

class AddExercisesForm(forms.ModelForm):
    
    rutine_exercises = forms.ModelMultipleChoiceField(
        queryset=Exercise.objects.all(),
        label='Ejercicios',
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'choices form-select form-control-lg multiple-remove',
            'id': 'rutine_exercises'
        })
    )

    class Meta:
        model = Rutine
        fields = ['rutine_exercises']
