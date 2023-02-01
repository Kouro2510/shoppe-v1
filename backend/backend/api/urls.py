from django.urls import path
from .views import UserRegisterView
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('api/register/', UserRegisterView.as_view()),
    path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='login'),
]
