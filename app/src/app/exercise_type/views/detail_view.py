from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.exercise_type.model import ExerciseType

class ExerciseTypeDetailView(LoginRequiredMixin, SuperAdminRequiredMixin, DetailView):
    model = ExerciseType
    template_name = 'exercise_type/detail.html'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de ejercicio'
        context['description'] = 'Todos los detalles de un tipo de ejercicio especifico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Ejercicios', 'url': 'exercise_type_list'},
            {'name': 'Detalle'}
        ]
        return context
