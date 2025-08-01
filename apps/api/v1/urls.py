from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('user/', include('apps.users.api.v1.urls.users')),
    path('coupon/', include('apps.coupons.api.v1.urls')),
    path('redemption/', include('apps.redemptions.api.v1.urls')),
]
