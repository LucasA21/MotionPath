from django.contrib.auth import get_user_model
from app.trainer.model import Trainer

def is_trainer(request):
    if request.user.is_authenticated:
        User = get_user_model()
        try:
            trainer = Trainer.objects.get(user=request.user)
            is_trainer = True
        except Trainer.DoesNotExist:
            is_trainer = False
    else:
        is_trainer = False
        
    return {'is_trainer': is_trainer}