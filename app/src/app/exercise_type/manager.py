from django.db import models

class ExerciseTypeManager(models.Manager):
    def get_default_table(self):
        return self.get_queryset().values('id', 'name')