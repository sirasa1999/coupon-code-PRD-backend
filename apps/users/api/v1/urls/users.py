from django.urls import path
from rest_framework import routers

from apps.users.api.v1.views import (
    UserAllDataViewSet,
    UserViewSet,
    CustomTokenViewBase)

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'', UserViewSet, basename='user')
router.register(r'session/me', UserAllDataViewSet, basename='me')


urlpatterns = [
    path('get-token/', CustomTokenViewBase.as_view(), name='token_obtain'),
]

urlpatterns += router.urls
