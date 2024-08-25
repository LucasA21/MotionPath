from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.difficulty_level.form import DifficultyLevelForm
from app.difficulty_level.model import DifficultyLevel
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

class DifficultyLevelCreateView(LoginRequiredMixin, SuperAdminRequiredMixin, CreateView):
    model = DifficultyLevel
    template_name = 'difficulty_level/create.html'
    form_class = DifficultyLevelForm

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Niveles de Dificultad'   
        context['description'] = 'Crear un nuevo nivel de dificultad.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Niveles de dificultad', 'url': 'difficulty_level_list'},
            {'name': 'Crear'}
        ]
        return context

    # override
    def get_success_url(self):
        return reverse_lazy('difficulty_level_detail', kwargs={'pk': self.object.pk})
   