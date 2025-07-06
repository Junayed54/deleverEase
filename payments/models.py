from django.db import models
from courier.models import Order

class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('succeeded', 'Succeeded'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_intent = models.CharField(max_length=255, unique=True)
    client_secret = models.CharField(max_length=255, blank=True, null=True)  # Optional, if you want to store it
    payment_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Helpful for tracking webhook updates

    def __str__(self):
        return f"Payment for Order #{self.order.id} - {self.payment_status}"
