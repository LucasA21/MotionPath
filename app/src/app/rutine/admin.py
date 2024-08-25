from django.contrib import admin

from app.rutine.model import Rutine

class RutineAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'difficulty_level', 'display_rutine_types', 'display_rutine_exercises', 'display_user_rutine')
    list_filter = ('user', 'difficulty_level', 'rutine_type', 'rutine_exercises', 'user_rutine')
    search_fields = ('name', 'user__username')
    raw_id_fields = ('user', 'difficulty_level', 'rutine_type', 'rutine_exercises', 'user_rutine')

    def display_rutine_types(self, obj):
        return ', '.join([rutine_type.name if rutine_type is not None else '' for rutine_type in obj.rutine_type.all()])
    
    def display_rutine_exercises(self, obj):
        return ', '.join([rutine_exercises.name if rutine_exercises is not None else '' for rutine_exercises in obj.rutine_exercises.all()])

    def display_user_rutine(self, obj):
        return ', '.join([user_rutine.email if user_rutine is not None else '' for user_rutine in obj.user_rutine.all()])

    display_rutine_types.short_description = 'Tipos de Rutina'
    display_rutine_exercises.short_description = 'Ejercicios'
    display_user_rutine.short_description = 'Usuario que eligieron'

admin.site.register(Rutine, RutineAdmin)
