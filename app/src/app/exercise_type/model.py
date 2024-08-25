from django.db import models

from app.exercise_type.manager import ExerciseTypeManager

class ExerciseType(models.Model):
    name = models.CharField(max_length=100)

    objects = ExerciseTypeManager()

    def __str__ (self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Ejercicio"
        verbose_name_plural = "Tipos de Ejercicios"
        ordering = ['name']
