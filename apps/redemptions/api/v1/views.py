from apps.core.permissions import IsAdminUser
from apps.redemptions.models import Redemption
from rest_framework import generics, permissions
from .serializers import RedemptionSerializer

class RedemptionListCreateView(generics.ListCreateAPIView):
    serializer_class = RedemptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Redemption.objects.filter(user=self.request.user)
    
class AdminRedemptionListView(generics.ListAPIView):
    queryset = Redemption.objects.all()
    serializer_class = RedemptionSerializer
    permission_classes = [IsAdminUser]
