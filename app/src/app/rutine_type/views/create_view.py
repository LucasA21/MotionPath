from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.rutine_type.form import RutineTypeForm
from app.rutine_type.model import RutineType


class RutineTypeCreateView(LoginRequiredMixin, SuperAdminRequiredMixin, CreateView):
    model = RutineType
    template_name = 'rutine_type/create.html'
    form_class = RutineTypeForm
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Tipos de Rutinas'   
        context['description'] = 'Crear un nuevo tipo de rutina.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Rutinas', 'url': 'rutine_type_list'},
            {'name': 'Crear'}
        ]
        return context

    # override
    def get_success_url(self):
        return reverse_lazy('rutine_type_detail', kwargs={'pk': self.object.pk})