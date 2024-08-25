from django.contrib import admin

from app.difficulty_level.model import DifficultyLevel

class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'user__username')

admin.site.register(DifficultyLevel, DifficultyLevelAdmin)