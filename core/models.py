import string

from django.db import models, transaction

from shortuuid.django_fields import ShortUUIDField


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class DiscountCode(models.Model):
    brand = models.ForeignKey(Brand, related_name='discount_codes', on_delete=models.CASCADE)

    code = ShortUUIDField(length=8, max_length=8, alphabet=f'{string.ascii_letters}{string.digits}', editable=False)
    models.UniqueConstraint(fields=['brand', 'code'], name='unique_brand_discount_code')
    valid = models.BooleanField(default=True)

    @classmethod
    def create_discount_codes(cls, brand_id, number_of_discount_codes):
        with transaction.atomic():
            for _ in range(number_of_discount_codes):
                instance = cls(brand_id=brand_id)
                instance.save()

    @classmethod
    def obtain_discount_code(cls, brand_id, customer_id):
        discount_code = cls.objects.filter(valid=True, brand__id=brand_id).first()
        discount_code.valid = False
        discount_code._customer_id = customer_id
        discount_code._discount_code = discount_code.id
        discount_code.save()

        return discount_code.code

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
