from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic import ListView

from app.rutine_type.model import RutineType

class RutineTypeListView(LoginRequiredMixin, SuperAdminRequiredMixin, ListView):
    model = RutineType
    template_name = 'rutine_type/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return RutineType.objects.get_default_table().order_by(*self.ordering)

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Rutinas'
        context['description'] = 'Listado de todos los tipos de rutinas.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de Rutinas'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['N° de referencia', RutineType._meta.get_field('name').verbose_name]
        context['rows'] = list(queryset.values_list('id', 'name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'rutine_type_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'rutine_type_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'rutine_type_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context