from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelListView(LoginRequiredMixin, SuperAdminRequiredMixin, ListView):
    model = DifficultyLevel
    template_name = 'difficulty_level/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return DifficultyLevel.objects.get_default_table().order_by(*self.ordering)

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Niveles de dificultad'
        context['description'] = 'Listado de todos los niveles de dificultad.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Niveles de Dificultad'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['N° de referencia', DifficultyLevel._meta.get_field('name').verbose_name]
        context['rows'] = list(queryset.values_list('id', 'name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'difficulty_level_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'difficulty_level_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'difficulty_level_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context