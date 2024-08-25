from django.db import models

from app.assign_rutine.manager import AssignRutineManager
from app.user.model import User
from app.trainer.model import Trainer
from app.rutine.model import Rutine

# Create your models here.
class AssignRutine(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT, verbose_name='Usuario')
    trainer = models.ForeignKey(Trainer, on_delete=models.RESTRICT, verbose_name='Entrenador')
    rutine = models.ForeignKey(Rutine, on_delete=models.RESTRICT, verbose_name='Rutina')

    objects = AssignRutineManager()

    def __str__(self):
        return f"""El entrenador: {self.trainer} le asigno al usuario: {self.user} la rutina: {self.rutine}."""
    
    class Meta:
        verbose_name = "Rutina asignada"
        verbose_name_plural = "Rutinas asignadas"
        ordering = ['user']