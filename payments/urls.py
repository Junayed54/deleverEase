from django.urls import path
from .views import CreatePaymentIntent, ConfirmPayment

urlpatterns = [
    path('api/payment/initialize/', CreatePaymentIntent.as_view()),
    path('api/payment/confirm/', ConfirmPayment.as_view()),
]
