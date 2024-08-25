from django.contrib import admin
from .model import Exercise

class ExerciseAdmin (admin.ModelAdmin):
    list_display = ('name', 'exercise_type', 'difficulty_level', 'user')
    list_filter = ('name', 'difficulty_level', 'exercise_type')
    search_fields = ('name', 'exercise_type')
    raw_id_fields = ('difficulty_level', 'exercise_type')

admin.site.register(Exercise, ExerciseAdmin)
