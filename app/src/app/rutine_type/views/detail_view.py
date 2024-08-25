from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic import DetailView

from app.rutine_type.model import RutineType


class RutineTypeDetailView(LoginRequiredMixin, SuperAdminRequiredMixin, DetailView):
    model = RutineType
    template_name = 'rutine_type/detail.html'
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Rutinas'
        context['description'] = 'Todos los detalles de un tipo de rutina especifica.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Rutinas', 'url': 'rutine_type_list'},
            {'name': 'Detalle'}
        ]
        return context