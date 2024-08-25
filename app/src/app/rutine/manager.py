from django.db import models
from django.db.models import CharField, Value
from django.db.models.functions import Concat
from django.contrib.postgres.aggregates import ArrayAgg


class RutineManager(models.Manager):
    def get_default_table(self):
        return self.get_queryset().annotate(
            full_name=Concat('user__last_name', Value(' '), 'user__first_name', output_field=CharField()),
            difficulty_level_name=models.F('difficulty_level__name'),
            rutine_types=ArrayAgg('rutine_type__name')
        ).values('name', 'full_name', 'difficulty_level_name', 'rutine_types')
    
    def get_own_table(self, logged_user):
        return self.get_queryset().filter(user=logged_user).annotate(
            full_name=Concat('user__last_name', Value(' '), 'user__first_name', output_field=CharField()),
            difficulty_level_name=models.F('difficulty_level__name'),
            rutine_types=ArrayAgg('rutine_type__name')
        ).values('name', 'full_name', 'difficulty_level_name', 'rutine_types')
    
    def get_picked_table(self, logged_user):
        return self.get_queryset().filter(user_rutine=logged_user).annotate(
            full_name=Concat('user__last_name', Value(' '), 'user__first_name', output_field=CharField()),
            difficulty_level_name=models.F('difficulty_level__name'),
            rutine_types=ArrayAgg('rutine_type__name')
        ).values('name', 'full_name', 'difficulty_level_name', 'rutine_types')
