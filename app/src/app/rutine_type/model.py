from django.db import models

from app.rutine_type.manager import RutineTypeManager

class RutineType(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")

    objects = RutineTypeManager()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Tipo de rutina"
        verbose_name_plural = "Tipos de rutina"
        ordering = ['name']