from django.contrib import admin
from app.assign_rutine.model import AssignRutine

class AssignRutineAdmin(admin.ModelAdmin):
    list_display = ('user', 'trainer', 'rutine')
    list_filter = ('user', 'trainer', 'rutine')
    raw_id_fields = ('user', 'trainer', 'rutine')

admin.site.register(AssignRutine, AssignRutineAdmin)
