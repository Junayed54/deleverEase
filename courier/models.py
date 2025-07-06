from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('assigned', 'Assigned'),
        ('delivered', 'Delivered'),
        ('complete', 'Complete'),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='orders')
    delivery_man = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='assigned_orders')
    address = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.status}"
