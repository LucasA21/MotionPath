from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.difficulty_level.form import DifficultyLevelForm
from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelUpdateView(LoginRequiredMixin, SuperAdminRequiredMixin, UpdateView):
    model = DifficultyLevel
    template_name = 'difficulty_level/update.html'
    form_class = DifficultyLevelForm
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Niveles de Dificultad'
        context['description'] = 'Actualizar un nivel de dificultad existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Niveles de Dificultad', 'url': 'difficulty_level_list'},
            {'name': 'Actualizar'}
        ]
        return context

    # override
    def get_success_url(self):
        return reverse_lazy('difficulty_level_detail', kwargs={'pk': self.object.pk})