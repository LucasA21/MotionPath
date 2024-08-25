from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.assign_rutine.model import AssignRutine


class AssignRutineDeleteView(LoginRequiredMixin, DeleteView):
    model = AssignRutine
    template_name = 'assign_rutine/delete.html'
    success_url = reverse_lazy('assign_rutine_list')
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Confirmar eliminación de asignación de rutina'
        return context


    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas asignadas'
        context['description'] = 'Eliminar la asignación de rutinas a un usuario de parte del entrenador.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas asignadas', 'url': 'assign_rutine_list'},
            {'name': 'Eliminar'}
        ]
        return context