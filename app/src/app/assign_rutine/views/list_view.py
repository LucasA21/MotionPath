from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.assign_rutine.model import AssignRutine

class AssignRutineListView(LoginRequiredMixin, ListView):
    model = AssignRutine
    template_name = 'assign_rutine/list.html'

    # override
    def get_queryset(self):
        return AssignRutine.objects.get_default_table()

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Rutinas asignadas'
        context['description'] = 'Listado de todas las asignaciones de rutinas a usuarios de parte de los entrenadores.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas asignadas'}
        ]

        queryset = self.get_queryset().values_list('id', 'user__email', 'trainer__user__email', 'rutine__name')
        context['headers'] = [
            'N° de referencia', 
            AssignRutine._meta.get_field('user').verbose_name,
            AssignRutine._meta.get_field('trainer').verbose_name,
            AssignRutine._meta.get_field('rutine').verbose_name
        ]
        context['rows'] = list(queryset)
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'assign_rutine_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'assign_rutine_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'assign_rutine_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context
