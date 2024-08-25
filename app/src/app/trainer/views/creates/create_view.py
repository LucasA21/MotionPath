from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.trainer.form import TrainerForm
from app.trainer.model import Trainer

class TrainerCreateView(LoginRequiredMixin, CreateView):
    model = Trainer
    template_name = 'trainer/creates/create.html'
    form_class = TrainerForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        context['title'] = 'Entrenadores'
        context['description'] = 'Crear un nuevo entrenador.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Entrenadores', 'url': 'trainer_list'},
            {'name': 'Crear'}
        ]
        return context

    def get_success_url(self):
        return reverse_lazy('trainer_detail', kwargs={'pk': self.object.pk})
