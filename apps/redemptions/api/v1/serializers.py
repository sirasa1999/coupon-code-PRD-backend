from rest_framework import serializers
from apps.coupons.constants import PRIVATE
from apps.redemptions.models import Redemption
from apps.coupons.models import Coupon
from django.utils import timezone

class RedemptionSerializer(serializers.ModelSerializer):
    coupon_code = serializers.CharField(write_only=True)
    coupon_name = serializers.CharField(source='coupon.code', read_only=True)

    class Meta:
        model = Redemption
        fields = ['id', 'coupon_code', 'coupon_name', 'redeemed_at']
        read_only_fields = ['id', 'redeemed_at']

    def validate_coupon_code(self, value):
        user = self.context['request'].user

        try:
            coupon = Coupon.objects.get(code=value)
        except Coupon.DoesNotExist:
            raise serializers.ValidationError("Invalid coupon code.")

        #Restrict private coupon access
        if coupon.type == PRIVATE and not user.is_staff:
            raise serializers.ValidationError("This coupon is private and cannot be used by you.")

        #Check if user already redeemed it
        if Redemption.objects.filter(user=user, coupon=coupon).exists():
            raise serializers.ValidationError("You have already redeemed this coupon.")

        #Check global max uses
        total_redemptions = Redemption.objects.filter(coupon=coupon).count()
        if coupon.max_uses is not None and total_redemptions >= coupon.max_uses:
            raise serializers.ValidationError("This coupon has crossed its maximum redemption.")
        
        #Coupon not yet active
        if coupon.valid_from and coupon.valid_from > timezone.now():
            raise serializers.ValidationError("This coupon is not yet active.")

        #Coupon expired
        if coupon.valid_to and coupon.valid_to < timezone.now():
            raise serializers.ValidationError("This coupon has expired.")

        return value


    def create(self, validated_data):
        user = self.context['request'].user
        coupon_code = validated_data.pop('coupon_code')

        try:
            coupon = Coupon.objects.get(code=coupon_code)
        except Coupon.DoesNotExist:
            raise serializers.ValidationError({'coupon_code': 'Invalid coupon code.'})

        return Redemption.objects.create(user=user, coupon=coupon)

