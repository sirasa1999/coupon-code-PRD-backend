from django.urls import path
from .views import RedemptionListCreateView, AdminRedemptionListView

urlpatterns = [
    path('', RedemptionListCreateView.as_view(), name='redemption-list-create'),
    path('admin', AdminRedemptionListView.as_view(), name='redemption-list-admin'),
]
