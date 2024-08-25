from django.db import models
from django.core.exceptions import ValidationError

from app.user.model import User
from app.difficulty_level.model import DifficultyLevel
from app.rutine_type.model import RutineType
from app.rutine.manager import RutineManager
from app.exercise.model import Exercise

class Rutine(models.Model):
    name = models.CharField(max_length=60, verbose_name="Nombre")
    user = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='rutines', verbose_name="Creador")
    difficulty_level = models.ForeignKey(DifficultyLevel, on_delete=models.RESTRICT, null=True, verbose_name="Nivel de Dificultad")
    rutine_type = models.ManyToManyField(RutineType, verbose_name="Tipo de Rutina")
    rutine_exercises = models.ManyToManyField(Exercise, verbose_name="Ejercicios")
    user_rutine = models.ManyToManyField(User, related_name='user_rutines', verbose_name="Usuarios de la Rutina")

    objects = RutineManager()

    def __str__(self):
        return self.name

    def clean(self):
        if self.difficulty_level is None:
            raise ValidationError("Debe especificar un nivel de dificultad para la rutina.")

    class Meta:
        verbose_name = "Rutina"
        verbose_name_plural = "Rutinas"
        ordering = ['name']
