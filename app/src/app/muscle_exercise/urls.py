from django.urls import path

import app.muscle_exercise.views as view

urlpatterns = [
    path('', view.MuscleExerciseListView.as_view(), name='muscle_exercise_list'),
    path('<int:pk>/', view.MuscleExerciseDetailView.as_view(), name='muscle_exercise_detail'),
    path('create/', view.MuscleExerciseCreateView.as_view(), name='muscle_exercise_create'),
    path('update/<int:pk>', view.MuscleExerciseUpdateView.as_view(), name='muscle_exercise_update'),
    path('delete/<int:pk>', view.MuscleExerciseDeleteView.as_view(), name='muscle_exercise_delete')
]