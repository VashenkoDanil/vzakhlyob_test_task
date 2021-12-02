from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.account.views import CreateUserViewSet, ActivateUsersView

urlpatterns = [
    path('register/', CreateUserViewSet.as_view(), name='register'),
    path('activate/<uidb64>/<token>/', ActivateUsersView.as_view(), name='activate'),
    path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
