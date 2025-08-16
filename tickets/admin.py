from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('subject', 'customer', 'category', 'status', 'created_at')
    list_filter = ('status', 'category')
    search_fields = ('subject', 'message', 'customer__username')
