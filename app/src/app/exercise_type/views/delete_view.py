from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.exercise_type.model import ExerciseType

class ExerciseTypeDeleteView(LoginRequiredMixin,SuperAdminRequiredMixin, DeleteView):
    model = ExerciseType
    template_name = 'exercise_type/delete.html'
    success_url = reverse_lazy('exercise_type_list')

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de ejercicios'
        context['description'] = 'Eliminar un tipo de ejercicio específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de ejercicio', 'url': 'exercise_type_list'},
            {'name': 'Eliminar'}
        ]
        return context