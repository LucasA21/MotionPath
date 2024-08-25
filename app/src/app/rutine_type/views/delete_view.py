from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from app.rutine_type.model import RutineType


class RutineTypeDeleteView(LoginRequiredMixin, SuperAdminRequiredMixin, DeleteView):
    model = RutineType
    template_name = 'rutine_type/delete.html'
    success_url = reverse_lazy('rutine_type_list')
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Rutinas'
        context['description'] = 'Eliminar un tipo de rutina específica.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Rutinas', 'url': 'rutine_type_list'},
            {'name': 'Eliminar'}
        ]
        return context
