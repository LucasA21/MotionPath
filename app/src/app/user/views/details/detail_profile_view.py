from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

from app.user.model import User

class UserDetailProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/details/detail_profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['description'] = 'Todos los detalles de un usuario específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'home'},
            {'name': 'Perfil'}
        ]
        return context
