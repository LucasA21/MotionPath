from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.exercise_type.form import ExerciseTypeForm
from app.exercise_type.model import ExerciseType

class ExerciseTypeUpdateView(LoginRequiredMixin, SuperAdminRequiredMixin, UpdateView):
    model = ExerciseType
    template_name = 'exercise_type/update.html'
    form_class = ExerciseTypeForm

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False
        
        context['title'] = 'Tipos de Ejercicios'
        context['description'] = 'Actualizar un tipo de ejercicio existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de ejercicio', 'url': 'exercise_type_list'},
            {'name': 'Actualizar'}
        ]
        return context
    
    # override
    def get_success_url(self):
        return reverse_lazy('exercise_type_detail', kwargs={'pk':self.object.pk})