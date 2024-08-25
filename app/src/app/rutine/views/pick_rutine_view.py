from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from app.rutine.forms.pick_rutine import PickRutineForm

class PickRutineView(LoginRequiredMixin, FormView):
    template_name = 'rutine/pick_rutine.html'
    form_class = PickRutineForm
    success_url = reverse_lazy('picked_rutine_list')

    def form_valid(self, form):
        selected_rutine = form.cleaned_data['rutine']
        self.request.user.user_rutines.add(selected_rutine)
        return super(PickRutineView, self).form_valid(form)
