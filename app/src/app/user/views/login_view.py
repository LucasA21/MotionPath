from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('dashboard')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid email or password.', extra_tags='error')
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('username')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            if remember_me:
                # Set the session to not expire
                request.session.set_expiry(1209600)  # 2 semanas
            else:
                # Set the session to expire when the browser closes
                request.session.set_expiry(0)
            return redirect(self.get_success_url())
        else:
            messages.error(request, 'Invalid email or password.', extra_tags='error')
            return self.form_invalid(self.get_form())

    def get_form(self):
        return super().get_form()
