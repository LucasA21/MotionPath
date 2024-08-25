from django.db import models

from app.muscle_exercise.manager import MuscleExerciseManager

class MuscleExercise (models.Model):
    name = models.CharField(max_length=100)

    objects = MuscleExerciseManager()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Músculo"
        verbose_name_plural = "Músculos"
        ordering = ['name']
