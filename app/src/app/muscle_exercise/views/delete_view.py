from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseDeleteView(LoginRequiredMixin, SuperAdminRequiredMixin, DeleteView):
    model = MuscleExercise
    template_name = 'muscle_exercise/delete.html'
    success_url = reverse_lazy('muscle_exercise_list')

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Músculos'
        context['description'] = 'Eliminar un músculo específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Músculos', 'url': 'muscle_exercise_list'},
            {'name': 'Eliminar'}
        ]
        return context