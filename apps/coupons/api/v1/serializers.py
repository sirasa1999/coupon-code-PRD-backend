from apps.core.serializers import DynamicFieldsModelSerializer
from rest_framework import serializers

from apps.coupons.models import Coupon

class CouponSerializer(DynamicFieldsModelSerializer):
    """
    Serializer for Coupon model.
    """
    class Meta:
        model = Coupon
        fields = '__all__'
        read_only_fields = ('created_at', 'is_archived')

