from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WaterDispenserViewSet
from rest_framework.authtoken.views import obtain_auth_token #Token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView #JWT

router = DefaultRouter()
router.register('dispensers', WaterDispenserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token), 
    # path('token/', views.LoginView.as_view(), name='token_obtain_pair'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
]