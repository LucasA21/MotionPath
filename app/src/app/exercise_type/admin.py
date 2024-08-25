from django.contrib import admin

from app.exercise_type.model import ExerciseType

class ExerciseTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'user__username')

admin.site.register(ExerciseType, ExerciseTypeAdmin)


