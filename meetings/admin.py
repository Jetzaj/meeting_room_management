from django.contrib import admin
from meetings.models import Room, RoomBooking


# Meeting room model
class RoomAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_time', 'updated_time')
    list_display = ('room_name', 'room_department', 'room_maintenance_name', 'room_maintenance_phone')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Room, RoomAdmin)


# Meeting room booking model
class RoomBookingAdmin(admin.ModelAdmin):
    exclude = ('booking_user', 'booking_user_name', 'created_time', 'updated_time')
    list_display = ('room', 'booking_user_name', 'booking_user_phone', 'start_time', 'end_time')

    def save_model(self, request, obj, form, change):
        obj.booking_user = request.user
        obj.booking_user_name = request.user.username
        super().save_model(request, obj, form, change)


admin.site.register(RoomBooking, RoomBookingAdmin)
