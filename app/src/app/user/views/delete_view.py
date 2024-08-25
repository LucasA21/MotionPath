from django.contrib.auth.mixins import LoginRequiredMixin
from project.mixins.super_user_mixin import SuperAdminRequiredMixin
from django.views.generic.edit import DeleteView
from django.db.models import ProtectedError
from django.contrib import messages
from django.shortcuts import redirect

from django.urls import reverse_lazy
from app.user.model import User

class UserDeleteView(LoginRequiredMixin, SuperAdminRequiredMixin, DeleteView):
    model = User
    template_name = 'user/delete.html'
    success_url = reverse_lazy('user_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(request, 'Usuario eliminado con éxito.')
        except ProtectedError:
            messages.error(request, 'No se puede eliminar este usuario porque está referenciado por otros registros.')
            return redirect(success_url)
        return redirect(success_url)
