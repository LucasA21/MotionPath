from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.muscle_exercise.form import MuscleExerciseForm
from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseCreateView(LoginRequiredMixin, SuperAdminRequiredMixin, CreateView):
    model = MuscleExercise
    template_name = 'muscle_exercise/create.html'
    form_class = MuscleExerciseForm
    
    # override
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Músculos'
        context['description'] = 'Crear un nuevo músculo.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Músculos', 'url': 'muscle_exercise_list'},
            {'name': 'Crear'}
        ]
        return context
    
    # override
    def get_success_url(self):
        return reverse_lazy('muscle_exercise_detail', kwargs={'pk': self.object.pk})