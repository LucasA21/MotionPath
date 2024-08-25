from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from app.trainer.model import Trainer

class TrainerListView(LoginRequiredMixin, ListView):
    model = Trainer
    template_name = 'trainer/list.html'
    context_object_name = 'trainers'
    ordering = ['id']

    def get_queryset(self):
        return Trainer.objects.all().order_by(*self.ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Entrenadores'
        context['description'] = 'Listado de todos los entrenadores.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Entrenadores'}
        ]

        queryset = self.get_queryset()
        context['headers'] = ['N° referencia', 'Email', 'Verificado']
        context['rows'] = queryset.values_list('id', 'user__email', 'is_verify')
        # TODO: ver si hace falta hacer botones para la lista de todos los entrenadores
        # context['table_actions'] = {
        #     'active': True,
        #     'buttons': [
        #         {
        #             'color': 'danger',
        #             'url': 'trainer_delete',
        #             'icon': 'trash',
        #             'pk': True
        #         },
        #         {
        #             'color': 'primary',
        #             'url': 'trainer_update',
        #             'icon': 'pencil',
        #             'pk': True
        #         },
        #         {
        #             'color': 'info',
        #             'url': 'trainer_detail',
        #             'icon': 'eye',
        #             'pk': True
        #         },
        #     ],
        # }

        return context
