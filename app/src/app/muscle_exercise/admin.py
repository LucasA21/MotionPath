from django.contrib import admin

from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'user__username')

admin.site.register(MuscleExercise, MuscleExerciseAdmin)