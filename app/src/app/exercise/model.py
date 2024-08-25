from django.db import models
from django.core.exceptions import ValidationError

from app.exercise_type.model import ExerciseType
from app.difficulty_level.model import DifficultyLevel
from app.user.model import User
from app.exercise.manager import ExerciseManager

class Exercise (models.Model):
    name = models.CharField(max_length=100)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.RESTRICT, null=True)
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.RESTRICT, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='exercises', null=True, blank=True)

    objects = ExerciseManager()

    def __str__ (self):
        return self.name

    def clean(self):
        if self.difficulty_level is None:
            raise ValidationError("Debe especificar un nivel de dificultad para el ejercicio.")
        if self.exercise_type is None:
            raise ValidationError("Debe especificar un tipo de ejercicio")
        if self.user is None:
            raise ValidationError("Debe especificar un usuario")
        
    class Meta:
        verbose_name = "Ejercicio"
        verbose_name_plural = "Ejercicios"
        ordering = ['name']