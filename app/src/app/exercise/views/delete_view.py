from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.exercise.model import Exercise

class ExerciseDeleteView(LoginRequiredMixin, DeleteView):
    model = Exercise
    template_name = 'exercise/delete.html'
    success_url = reverse_lazy('exercise_list')

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ejercicios'
        context['description'] = 'Eliminar un ejercicio específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url' : 'dashboard'},
            {'name': 'Ejercicios', 'url': 'exercise_list'},
            {'name': 'Eliminar'}
        ]
        return context
    