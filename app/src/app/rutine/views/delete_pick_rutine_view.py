from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from app.rutine.model import Rutine
from app.rutine.forms.form import RutineForm

class DeletePickRutineView(LoginRequiredMixin, FormView):
    template_name = 'rutine/delete_picked_rutine.html'
    form_class = RutineForm
    success_url = reverse_lazy('picked_rutine_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rutine_id = self.kwargs['pk']
        context['object'] = get_object_or_404(Rutine, id=rutine_id)
        return context

    def post(self, request, *args, **kwargs):
        rutine_id = self.kwargs['pk']
        rutine = get_object_or_404(Rutine, id=rutine_id)
        request.user.user_rutines.remove(rutine)
        return super().form_valid(form=None)
