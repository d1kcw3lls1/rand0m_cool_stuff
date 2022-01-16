import string

from django.db import models

from shortuuid.django_fields import ShortUUIDField


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class DiscountCode(models.Model):
    brand = models.ForeignKey(Brand, related_name='discount_codes', on_delete=models.CASCADE)

    code = ShortUUIDField(length=8, max_length=8, alphabet=f'{string.ascii_letters}{string.digits}', editable=False)
    models.UniqueConstraint(fields=['brand', 'code'], name='unique_brand_discount_code')
    valid = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.brand} - {self.code}'


class CustomerDiscountCode(models.Model):
    customer = models.ForeignKey(Customer, related_name='customers', on_delete=models.CASCADE, editable=False)
    discount_code = models.ForeignKey(
        DiscountCode, related_name='discount_codes', on_delete=models.CASCADE, editable=False
    )
    models.UniqueConstraint(fields=['customer', 'discount_code'], name='unique_customer_discount_code')

    def __str__(self):
        return f'{self.customer} - {self.discount_code}'
