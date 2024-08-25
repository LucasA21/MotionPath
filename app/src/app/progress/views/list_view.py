from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from django.db.models import Value, CharField
from django.db.models.functions import Concat

from app.progress.model import Progress

class ProgressListView(LoginRequiredMixin, ListView):
    model = Progress
    template_name = 'progress/list.html'
    context_object_name = 'progresses'
    ordering = ['id']

    def get_queryset(self):
        queryset = Progress.objects.annotate(
            exercises_names=Concat('exercises__name', Value(', '), output_field=CharField())
        ).values('id', 'user__email', 'weight', 'repetitions', 'exercises_names').distinct().order_by(*self.ordering)
        
        # Imprime el queryset para depuración
        for entry in queryset:
            print(f"ID: {entry['id']}, Email: {entry['user__email']}, Peso: {entry['weight']}, Repeticiones: {entry['repetitions']}, Ejercicios: {entry['exercises_names']}")
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Progresos'
        context['description'] = 'Listado de todos los progresos.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Progresos'}
        ]

        queryset = self.get_queryset()
        rows = []
        for item in queryset:
            row = [
                item['id'],
                item['user__email'],
                item['weight'],
                item['repetitions'],
                item['exercises_names']
            ]
            rows.append(row)
        
        context['headers'] = ['ID', 'Email', 'Peso', 'Repeticiones', 'Ejercicios']
        context['rows'] = rows
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'danger',
                    'url': 'progress_delete',
                    'icon': 'trash',
                    'pk': True
                },
                {
                    'color': 'primary',
                    'url': 'progress_update',
                    'icon': 'pencil',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'progress_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }

        return context
