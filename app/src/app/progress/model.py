from django.db import models
from app.user.model import User  # Asegúrate de que el import sea correcto
from app.exercise.model import Exercise

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercises = models.ManyToManyField(Exercise)
    weight = models.FloatField()
    repetitions = models.IntegerField() 
    
    def __str__(self):
        return f"{self.user.email} - Progress"
