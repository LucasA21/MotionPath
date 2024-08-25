from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.exercise.model import Exercise

class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = Exercise
    template_name = 'exercise/detail.html'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ejercicios'
        context['description'] = 'Todos los detalles de un ejercicio especifico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Ejercicios', 'url': 'exercise_list'},
            {'name': 'Detalle'}
        ]
        return context