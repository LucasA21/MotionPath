from django.contrib.auth.mixins import UserPassesTestMixin

class SuperAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser