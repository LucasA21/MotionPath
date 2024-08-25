from django.db import models
from django.db.models import CharField, Value
from django.db.models.functions import Concat
from django.contrib.postgres.aggregates import ArrayAgg


class ExerciseManager(models.Manager):
    def get_default_table(self):
        return self.get_queryset().annotate(
            full_name=Concat('user__last_name', Value(' '), 'user__first_name', output_field=CharField()),
            difficulty_level_name=models.F('difficulty_level__name'),
            exercise_types=ArrayAgg('exercise_type__name')
        ).values('name', 'full_name', 'difficulty_level_name', 'exercise_types')
