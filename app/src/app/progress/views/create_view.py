from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.progress.model import Progress
from app.progress.form import ProgressForm

class ProgressCreateView(LoginRequiredMixin, CreateView):
    model = Progress
    template_name = 'progress/create.html'
    form_class = ProgressForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        form.save_m2m()  # Esto asegura que los muchos-a-muchos se guarden correctamente
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = False
        context['title'] = 'Progresos'
        context['description'] = 'Crear un nuevo progreso.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Progresos', 'url': 'progress_list'},
            {'name': 'Crear'}
        ]
        return context

    def get_success_url(self):
        return reverse_lazy('progress_detail', kwargs={'pk': self.object.pk})

