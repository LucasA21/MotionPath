from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.rutine.model import Exercise

class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercise/list.html'
    ordering = ['id']

    # override 
    def get_queryset(self):
        return Exercise.objects.get_default_table().order_by(*self.ordering)
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ejercicios'
        context['description'] = 'Listado de todos los ejercicios.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Ejercicios'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['N° de referencia', Exercise._meta.get_field('name').verbose_name]
        context['rows'] = list(queryset.values_list('id', 'name'))
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'exercise_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url':'exercise_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url':'exercise_detail',
                    'icon': 'eye',
                    'pk': True
                }
            ]
        }

        return context