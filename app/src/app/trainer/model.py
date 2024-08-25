from django.db import models
from app.user.model import User

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_verify = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='user_trainer') ## relacion n a n entre usuarios y entrenadores 
     
    def __str__(self):
        return f"{self.user.email} - Trainer"
