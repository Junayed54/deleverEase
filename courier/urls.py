from django.urls import path
from .views import (
    OrderListView, OrderDetailView, OrderCreateView,
    AssignDeliveryManView, UpdateOrderStatusView
)

urlpatterns = [
    path('api/orders/', OrderListView.as_view(), name='order-list'),
    path('api/orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('api/orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('api/orders/<int:pk>/assign-delivery-man/', AssignDeliveryManView.as_view(), name='assign-delivery'),
    path('api/orders/<int:pk>/update-status/', UpdateOrderStatusView.as_view(), name='update-status'),
]
