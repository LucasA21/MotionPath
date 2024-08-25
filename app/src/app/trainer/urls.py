from django.urls import path

import app.trainer.views as view

urlpatterns = [
    path('', view.TrainerListView.as_view(), name='trainer_list'),
    path('<int:pk>/', view.TrainerDetailView.as_view(), name='trainer_detail'),
    path('create/', view.TrainerCreateView.as_view(), name='trainer_create'),
    path('update/<int:pk>/', view.TrainerUpdateView.as_view(), name='trainer_update'),
    path('delete/<int:pk>/', view.TrainerDeleteView.as_view(), name='trainer_delete'),
    path('make-trainer/', view.MakeTrainerView.as_view(), name='trainer_make'),
]
