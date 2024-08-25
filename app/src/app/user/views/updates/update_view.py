from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from app.user.forms.form import UserForm

from app.user.model import User

class UserUpdateView(LoginRequiredMixin, SuperAdminRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update.html'

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['title'] = 'Usuarios'
        context['description'] = 'Actualizar un usuario existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'home'},
            {'name': 'Usuarios', 'url': 'user_list'},
            {'name': 'Actualizar'}
        ]
        return context