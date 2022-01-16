from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomerDiscountCode, DiscountCode


@receiver(post_save, sender=DiscountCode)
def create_customer_discount_code(sender, instance, created, **kwargs):
    customer_id = getattr(instance, '_customer_id', None)
    discount_code = getattr(instance, '_discount_code', None)

    updated = not created
    valid_field_updated = customer_id and discount_code

    if updated and valid_field_updated:
        customer_discount_code = CustomerDiscountCode(customer_id=customer_id, discount_code_id=discount_code)
        customer_discount_code.save()
