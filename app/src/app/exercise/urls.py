from django.urls import path

import app.exercise.views as view

urlpatterns = [
    path('', view.ExerciseListView.as_view(), name='exercise_list'),
    path('<int:pk>', view.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('create/', view.ExerciseCreateView.as_view(), name='exercise_create'),
    path('update/<int:pk>', view.ExerciseUpdateView.as_view(), name='exercise_update'),
    path('delete/<int:pk>', view.ExerciseDeleteView.as_view(), name='exercise_delete'),
]