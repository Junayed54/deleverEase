from rest_framework import serializers
from .models import Payment
from courier.models import Order

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'order', 'amount', 'stripe_payment_intent', 'payment_status', 'created_at']


class StripePaymentIntentSerializer(serializers.Serializer):
    order_id = serializers.IntegerField()

    def validate_order_id(self, value):
        try:
            order = Order.objects.get(id=value)
        except Order.DoesNotExist:
            raise serializers.ValidationError("Order not found.")
        return value
