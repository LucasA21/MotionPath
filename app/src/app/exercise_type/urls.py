from django.urls import path

import app.exercise_type.views as view

urlpatterns = [
    path('', view.ExerciseTypeListView.as_view(), name='exercise_type_list'),
    path('<int:pk>/', view.ExerciseTypeDetailView.as_view(), name='exercise_type_detail'),
    path('create/', view.ExerciseTypeCreateView.as_view(), name='exercise_type_create'),
    path('update/<int:pk>/', view.ExerciseTypeUpdateView.as_view(), name='exercise_type_update'),
    path('delete/<int:pk>/', view.ExerciseTypeDeleteView.as_view(), name='exercise_type_delete'),
]
