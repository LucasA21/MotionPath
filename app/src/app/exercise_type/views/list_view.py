from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from project.mixins.super_user_mixin import SuperAdminRequiredMixin

from app.exercise_type.model import ExerciseType

class ExerciseTypeListView(LoginRequiredMixin, SuperAdminRequiredMixin, ListView):
    model = ExerciseType
    template_name = 'exercise_type/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return ExerciseType.objects.get_default_table().order_by(*self.ordering)
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tipos de Ejercicios'
        context['description'] = 'Listado de todos los tipos de ejercicios.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Tipos de ejercicios'}
        ]
    
        queryset = self.get_queryset()
        context['headers'] = ['N° de referencia', ExerciseType._meta.get_field('name').verbose_name]
        context['rows'] = list(queryset.values_list('id', 'name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'exercise_type_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'exercise_type_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'exercise_type_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }
        
        return context