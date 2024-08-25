from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelDeleteView(LoginRequiredMixin, SuperAdminRequiredMixin, DeleteView):
    model = DifficultyLevel
    template_name = 'difficulty_level/delete.html'
    success_url = reverse_lazy('difficulty_level_list')

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Niveles de Dificultad'
        context['description'] = 'Eliminar un nivel de dificultad.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Niveles de Dificultad', 'url': 'difficulty_level_list'},
            {'name': 'Eliminar'}
        ]
        return context
