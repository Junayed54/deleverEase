import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Payment
from .serializers import StripePaymentIntentSerializer
from courier.models import Order
from deliverEase.permissions import IsUser  # Assuming custom permission exists
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntent(APIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]

    def post(self, request):
        serializer = StripePaymentIntentSerializer(data=request.data)
        if not serializer.is_valid():
            field, messages = next(iter(serializer.errors.items()))
            message = messages[0] if isinstance(messages, list) else messages
            return Response({
                "success": False,
                "message": "Validation error occurred.",
                "errorDetails": {
                    "field": field,
                    "message": message
                }
            }, status=status.HTTP_400_BAD_REQUEST)

        order_id = serializer.validated_data['order_id']
        try:
            order = Order.objects.get(id=order_id, user=request.user)
        except Order.DoesNotExist:
            return Response({
                "success": False,
                "message": "Order not found.",
                "errorDetails": None
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            intent = stripe.PaymentIntent.create(
                amount=int(order.delivery_fee * 100),  # amount in cents
                currency='usd',
                metadata={'order_id': str(order.id)}
            )
        except Exception as e:
            return Response({
                "success": False,
                "message": "Stripe payment intent creation failed.",
                "errorDetails": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        payment, created = Payment.objects.get_or_create(order=order)

        # Always update these fields to reflect the current payment intent and status
        payment.amount = order.delivery_fee
        payment.stripe_payment_intent = intent['id']
        payment.payment_status = 'pending'
        payment.save()


        return Response({
            "success": True,
            "message": "Payment intent created successfully.",
            "data": {
                "client_secret": intent['client_secret'],
                "payment_intent_id": intent['id']
            }
        }, status=status.HTTP_201_CREATED)


class ConfirmPayment(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        intent_id = request.data.get("payment_intent_id")
        if not intent_id:
            return Response({
                "success": False,
                "message": "Missing payment_intent_id",
                "errorDetails": None
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            intent = stripe.PaymentIntent.retrieve(intent_id)
        except Exception as e:
            return Response({
                "success": False,
                "message": "Failed to retrieve payment intent.",
                "errorDetails": str(e)
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.objects.get(stripe_payment_intent=intent_id)
        except Payment.DoesNotExist:
            return Response({
                "success": False,
                "message": "Payment not found.",
                "errorDetails": None
            }, status=status.HTTP_404_NOT_FOUND)

        payment.payment_status = intent.status
        payment.save()
        print(intent.status)
        if intent.status == "succeeded":
            order = payment.order
            order.paid = True
            order.status = "assigned"  # Update order status upon successful payment
            order.save()

        return Response({
            "success": True,
            "message": "Payment confirmed.",
            "data": {
                "status": intent.status
            }
        }, status=status.HTTP_200_OK)
