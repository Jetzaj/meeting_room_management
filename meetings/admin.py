from django.contrib import admin
from meetings.models import Room


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_time', 'updated_time')
    list_display = ('room_name', 'room_department', 'room_maintenance_name', 'room_maintenance_phone')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Room, RoomAdmin)
