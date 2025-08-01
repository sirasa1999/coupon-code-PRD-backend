from apps.core.permissions import IsAdminUser
from apps.core.viewsets import CustomModelViewSet
from apps.coupons.api.v1.serializers import CouponSerializer
from apps.coupons.models import Coupon

from rest_framework.response import Response
from rest_framework import status


class CouponViewSet(CustomModelViewSet):
    """
    ViewSet for managing coupons.
    """
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        ''' for soft delete '''
        instance = self.get_object()
        instance.is_archived = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)