from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from app.rutine.model import Rutine

class OwnRutineListView(LoginRequiredMixin, ListView):
    model = Rutine
    template_name = 'rutine/list.html'
    ordering = ['id']

    # override
    def get_queryset(self):
        return Rutine.objects.get_own_table(self.request.user.id)

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.model._meta.verbose_name_plural
        context['description'] = 'Listado de todas las rutinas creadas por usted.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas propias'}
        ]

        queryset = self.get_queryset()
        context['headers'] = [
            'N° referencia',
            self.model._meta.get_field('name').verbose_name,
            self.model._meta.get_field('difficulty_level').verbose_name,
            self.model._meta.get_field('rutine_type').verbose_name
        ]
        context['rows'] = queryset.values_list(
            'id',
            'name',
            'difficulty_level_name',
            'rutine_types'
        )
        context['table_actions'] = {
            'active': True,
            'buttons': [
                {
                    'color': 'success',
                    'url': 'rutine_add_exercises',
                    'icon': 'plus-lg',
                    'pk': True
                },
                {
                    'color': 'info',
                    'url': 'own_rutine_detail',
                    'icon': 'eye',
                    'pk': True
                },
            ],
        }
        return context
