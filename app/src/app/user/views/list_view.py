from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic.list import ListView

from app.user.model import User

class UserListView(LoginRequiredMixin, SuperAdminRequiredMixin, ListView):
    model = User
    template_name = 'user/list.html'
    context_object_name = 'users'
    ordering = ['id']

    def get_queryset(self):
        return User.objects.all().order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Usuarios'
        context['description'] = 'Listado de todos los usuarios.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'home'},
            {'name': 'Usuarios'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['ID', 'Nombre', 'Apellido', 'Email']
        context['rows'] = queryset.values_list('id', 'first_name', 'last_name', 'email')
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'user_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'user_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'user_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }
        return context