from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.trainer.model import Trainer

class TrainerDetailView(LoginRequiredMixin, DetailView):
    model = Trainer
    template_name = 'trainer/detail.html'
    context_object_name = 'trainer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Entrenadores'
        context['description'] = 'Todos los detalles de un entrenador específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Entrenadores', 'url': 'trainer_list'},
            {'name': 'Detalle'}
        ]
        return context
