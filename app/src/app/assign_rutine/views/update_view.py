from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.assign_rutine.form import AssignRutineForm
from app.assign_rutine.model import AssignRutine

class AssignRutineUpdateView(LoginRequiredMixin, UpdateView):
    model = AssignRutine
    template_name = 'assign_rutine/update.html'
    form_class = AssignRutineForm

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Rutinas asignadas'
        context['description'] = 'Actualizar la asignación de rutinas a un usuario de parte del entrenador.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas asignadas', 'url': 'assign_rutine_list'},
            {'name': 'Actualizar'}
        ]
        return context

    # override
    def get_success_url(self):
        return reverse_lazy('assign_rutine_detail', kwargs={'pk': self.object.pk})
