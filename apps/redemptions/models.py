from django.db import models
from django.conf import settings
from apps.coupons.models import Coupon

class Redemption(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE)
    redeemed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'coupon')
