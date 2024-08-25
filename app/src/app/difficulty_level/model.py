from django.db import models

from app.difficulty_level.manager import DifficultyLevelManager

class DifficultyLevel(models.Model):
    name = models.CharField(max_length=100)

    objects = DifficultyLevelManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Nivel de dificultad"
        verbose_name_plural = "Niveles de dificultad"
        ordering = ['name']