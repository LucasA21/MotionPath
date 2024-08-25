from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from app.rutine.forms.form import RutineForm
from app.rutine.model import Rutine

class RutineUpdateView(LoginRequiredMixin, UpdateView):
    model = Rutine
    template_name = 'rutine/updates/update.html'
    form_class = RutineForm
    
    # override
    def get_success_url(self):
        return reverse_lazy('rutine_detail', kwargs={'pk': self.object.pk})

    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = self.model._meta.verbose_name_plural
        context['description'] = 'Actualizar una rutina existente.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas', 'url': 'rutine_list'},
            {'name': 'Actualizar'}
        ]
        return context