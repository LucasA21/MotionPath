from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.progress.form import ProgressForm
from app.progress.model import Progress

class ProgressUpdateView(LoginRequiredMixin, UpdateView):
    model = Progress
    template_name = 'progress/update.html'
    form_class = ProgressForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()  # Esto asegura que los muchos-a-muchos se guarden correctamente
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('progress_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True
        context['title'] = 'Progresos'
        context['description'] = 'Actualizar un progreso existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Progresos', 'url': 'progress_list'},
            {'name': 'Actualizar'}
        ]
        return context
