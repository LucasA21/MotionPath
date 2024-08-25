from django.db import models

class AssignRutineManager(models.Manager):
    def get_default_table(self):
        return self.get_queryset().values('id', 'user__email', 'trainer__user__email', 'rutine__name')
