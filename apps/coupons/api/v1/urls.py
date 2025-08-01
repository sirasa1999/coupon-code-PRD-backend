from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.coupons.api.v1.views import CouponViewSet

urlpatterns = [
]

router = DefaultRouter()
router.register(r'', CouponViewSet, basename='coupon')

urlpatterns += router.urls