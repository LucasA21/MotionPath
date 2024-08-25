from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home/dashboard.html'
    login_url = 'home/user_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'MotionPath'
        context['description'] = 'Pagina de inicio de MotionPath.'
        context['breadcrumb_items'] = [
            {'name': 'Inicio'},
        ]
        return context
