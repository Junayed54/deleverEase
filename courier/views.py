from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.shortcuts import get_object_or_404

from .models import Order
from .serializers import OrderSerializer, CreateOrderSerializer



from deliverEase.permissions import *
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Order.objects.all()
        elif user.role == 'delivery':
            return Order.objects.filter(delivery_man=user)
        return Order.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "success": True,
            "statusCode": 200,
            "message": "Orders fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class OrderDetailView(RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Order.objects.all()
        elif user.role == 'delivery':
            return Order.objects.filter(delivery_man=user)
        return Order.objects.filter(user=user)


class OrderCreateView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsUser]
    serializer_class = CreateOrderSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AssignDeliveryManView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def patch(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        delivery_man_id = request.data.get('delivery_man_id')
        if not delivery_man_id:
            return Response({
                "success": False,
                "message": "Delivery man ID is required.",
                "errorDetails": None
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # delivery_man_id = int(delivery_man_id)
            delivery_man = User.objects.get(id=int(delivery_man_id), role='delivery')
        except User.DoesNotExist:
            return Response({
                "success": False,
                "message": "Invalid delivery man ID.",
                "errorDetails": None
            }, status=status.HTTP_400_BAD_REQUEST)

        # ✅ Assign delivery man and update status
        order.delivery_man = delivery_man
        order.status = 'assigned'  # <-- Set status to 'assigned'
        order.save()
        return Response({
            "success": True,
            "message": "Delivery man assigned successfully.",
            "data": OrderSerializer(order).data
        }, status=status.HTTP_200_OK)



class UpdateOrderStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsDeliveryMan]

    def patch(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        if order.delivery_man != request.user:
            return Response({
                "success": False,
                "message": "Unauthorized access.",
                "errorDetails": "You must be the assigned delivery man to update this order."
            }, status=status.HTTP_403_FORBIDDEN)

        new_status = request.data.get("status")
        valid_statuses = ['pending','delivered', 'complete']
        if new_status not in valid_statuses:
            return Response({
                "success": False,
                "message": "Invalid status value.",
                "errorDetails": f"Status must be one of {valid_statuses}."
            }, status=status.HTTP_400_BAD_REQUEST)

        order.status = new_status
        order.save()
        return Response({
            "success": True,
            "message": "Order status updated successfully.",
            "data": OrderSerializer(order).data
        }, status=status.HTTP_200_OK)
