from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.assign_rutine.model import AssignRutine

class AssignRutineDetailView(LoginRequiredMixin, DetailView):
    model = AssignRutine
    template_name = 'assign_rutine/detail.html'

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas asignadas'
        context['description'] = 'Todos los detalles de una asignación de rutina especifica.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas asignadas', 'url': 'assign_rutine_list'},
            {'name': 'Detalle'}
        ]
        return context
