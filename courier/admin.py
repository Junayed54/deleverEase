from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'delivery_man', 'status', 'delivery_fee', 'paid', 'created_at')
    list_filter = ('status', 'paid', 'created_at')
    search_fields = ('user__email', 'delivery_man__email', 'address')
    readonly_fields = ('created_at',)

    raw_id_fields = ('user', 'delivery_man')  # Makes selection easier if many users

    ordering = ('-created_at',)
