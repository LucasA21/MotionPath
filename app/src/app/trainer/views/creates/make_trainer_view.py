from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.trainer.form import TrainerForm
from app.trainer.model import Trainer

class MakeTrainerView(LoginRequiredMixin, CreateView):
    model = Trainer
    template_name = 'trainer/creates/make_trainer.html'
    fields = []
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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