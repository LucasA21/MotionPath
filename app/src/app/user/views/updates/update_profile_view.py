from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from app.user.forms.form import UserForm

from app.user.model import User

class UserUpdateProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'user/update.html'
    success_url = reverse_lazy('user_detail_profile')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['title'] = 'Usuarios'
        context['description'] = 'Actualizar un usuario existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'home'},
            {'name': 'Perfil', 'url': 'user_detail_profile'},
            {'name': 'Actualizar'}
        ]
        return context