from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.rutine.forms.add_exercises import AddExercisesForm
from app.rutine.model import Rutine

class AddExercisesView(LoginRequiredMixin, UpdateView):
    model = Rutine
    template_name = 'rutine/updates/add_exercises.html'
    form_class = AddExercisesForm
    
    # override
    def get_success_url(self):
        return reverse_lazy('rutine_detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.model._meta.verbose_name_plural
        context['description'] = 'Agregar ejercicios a una rutina creada.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas', 'url': 'rutine_list'},
            {'name': 'Actualizar'}
        ]
        return context