from django.contrib import admin

from app.rutine_type.model import RutineType

class RutineTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'user__username')

admin.site.register(RutineType, RutineTypeAdmin)