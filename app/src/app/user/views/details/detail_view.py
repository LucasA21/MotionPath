from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic.detail import DetailView

from app.user.model import User

class UserDetailView(LoginRequiredMixin, SuperAdminRequiredMixin, DetailView):
    model = User
    template_name = 'user/details/detail.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['description'] = 'Todos los detalles de un usuario específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'home'},
            {'name': 'Usuarios', 'url': 'user_list'},
            {'name': 'Detalle'}
        ]
        return context
