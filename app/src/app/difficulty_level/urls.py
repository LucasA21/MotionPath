from django.urls import path

import app.difficulty_level.views as view

urlpatterns = [
    path('', view.DifficultyLevelListView.as_view(), name='difficulty_level_list'),
    path('<int:pk>', view.DifficultyLevelDetailView.as_view(), name='difficulty_level_detail'),
    path('create/', view.DifficultyLevelCreateView.as_view(), name='difficulty_level_create'),
    path('update/<int:pk>', view.DifficultyLevelUpdateView.as_view(), name='difficulty_level_update'),
    path('delete/<int:pk>', view.DifficultyLevelDeleteView.as_view(), name='difficulty_level_delete'),
]