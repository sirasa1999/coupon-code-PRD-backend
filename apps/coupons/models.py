from django.db import models
from apps.coupons.constants import CODE_TYPE

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 10.00 = 10%
    type = models.CharField(max_length=10, choices=CODE_TYPE)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    max_uses = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)

    def str(self):
        return self.code