from django.contrib import admin
from .models import Hotel, Booking, Feedback

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'stars', 'price_per_night')
    list_display_links = ('id', 'name')
    list_editable = ('stars', 'price_per_night') 
    list_filter = ('city', 'stars')
    search_fields = ('name', 'city')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'hotel', 'checkin', 'checkout', 'created_at')
    list_filter = ('hotel', 'created_at', 'checkin')
    search_fields = ('user__username', 'hotel__name')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)