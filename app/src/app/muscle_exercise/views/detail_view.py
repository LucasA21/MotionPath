from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseDetailView(LoginRequiredMixin, SuperAdminRequiredMixin, DetailView):
    model = MuscleExercise
    template_name = 'muscle_exercise/detail.html'
    

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Músculos'
        context['description'] = 'Todos los detalles de un músculo especifíco.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Músculos', 'url': 'muscle_exercise_list'},
            {'name': 'Detalle'}
        ]
        return context