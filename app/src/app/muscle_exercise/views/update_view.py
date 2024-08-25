from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.muscle_exercise.form import MuscleExerciseForm
from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseUpdateView(LoginRequiredMixin, SuperAdminRequiredMixin, UpdateView):
    model = MuscleExercise
    template_name = 'muscle_exercise/update.html'
    form_class = MuscleExerciseForm
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Músculos'
        context['description'] = 'Actualizar un músculo existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Músculos', 'url': 'muscle_exercise_list'},
            {'name': 'Actualizar'}
        ]
        return context

    # override
    def get_success_url(self):
        return reverse_lazy('muscle_exercise_detail', kwargs={'pk': self.object.pk})