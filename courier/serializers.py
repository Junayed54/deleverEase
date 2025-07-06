from rest_framework import serializers
from .models import Order
from users.serializers import UserProfileSerializer

class OrderSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    delivery_man = UserProfileSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id', 'user', 'delivery_man',
            'address', 'status', 'delivery_fee', 'paid', 'created_at'
        ]


class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['address', 'delivery_fee']
