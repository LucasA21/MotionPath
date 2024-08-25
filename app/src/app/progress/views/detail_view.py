from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from app.progress.model import Progress

class ProgressDetailView(LoginRequiredMixin, DetailView):
    model = Progress
    template_name = 'progress/detail.html'
    context_object_name = 'progress'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Progresos'
        context['description'] = 'Todos los detalles de un progreso específico.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Progresos', 'url': 'progress_list'},
            {'name': 'Detalle'}
        ]
        return context
