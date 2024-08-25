from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from app.rutine.forms.form import RutineForm
from app.rutine.model import Rutine

class RutineCreateView(LoginRequiredMixin, CreateView):
    model = Rutine
    template_name = 'rutine/create.html'
    form_class = RutineForm

    # override
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # override
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['is_update'] = True
        else:
            context['is_update'] = False

        context['title'] = 'Rutinas'
        context['description'] = 'Crear una nueva rutina.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio', 'url': 'dashboard'},
            {'name': 'Rutinas', 'url': 'rutine_list'},
            {'name': 'Crear'}
        ]
        return context
    
    # override
    def get_success_url(self):
        return reverse_lazy('rutine_detail', kwargs={'pk': self.object.pk})