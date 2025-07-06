from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('order__id', 'stripe_payment_intent')
    readonly_fields = ('created_at',)

    # Optional: prevent editing certain fields after creation
    def has_delete_permission(self, request, obj=None):
        # Customize if needed
        return super().has_delete_permission(request, obj)

    def has_add_permission(self, request):
        # Payments are usually created programmatically, optionally disable manual add
        return super().has_add_permission(request)

