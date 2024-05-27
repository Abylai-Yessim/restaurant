from django.contrib import admin
from .models import *
from .forms import *

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    form = MenuItemForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    pass
    
def mark_as_booked(modeladmin, request, queryset):
    for table in queryset:
        if table not in SiteSettings.objects.first().booked_tables.all():
            SiteSettings.objects.first().booked_tables.add(table)
    modeladmin.message_user(request, "Selected tables were successfully marked as booked.")
mark_as_booked.short_description = "Mark selected tables as booked"

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['number', 'is_reserved_display']

    def is_reserved_display(self, obj):
        return 'X' if obj.is_reserved else 'Available'

    is_reserved_display.short_description = 'Is Reserved'



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'table_number', 'time', 'phone']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'text')
    
@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['phone_number']