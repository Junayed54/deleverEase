from django.urls import path
from .views import RegisterView, LoginView, ProfileView

urlpatterns = [
    path('api/register/', RegisterView.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/profile/', ProfileView.as_view()),
]
