from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelDetailView(LoginRequiredMixin, SuperAdminRequiredMixin, DetailView):
    model = DifficultyLevel
    template_name = 'difficulty_level/detail.html'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Niveles de Dificultad'
        context['description'] = 'Todos los detalles de un nivel de dificultad.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Niveles de Dificultad', 'url': 'difficulty_level_list'},
            {'name': 'Detalle'}
        ]
        return context