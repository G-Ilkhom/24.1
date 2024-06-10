from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import PaymentListAPIView, UserCreateAPIView, UserDestroyApiView, UserRetrieveApiView, UserUpdateApiView

app_name = UsersConfig.name

urlpatterns = [
    path("payment/", PaymentListAPIView.as_view(), name="payment"),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path("<int:pk>/", UserRetrieveApiView.as_view(), name="users_retrieve"),
    path(
        "<int:pk>/delete/", UserDestroyApiView.as_view(), name="users_delete"
    ),
    path("<int:pk>/update/", UserUpdateApiView.as_view(), name="users_update"),
]



