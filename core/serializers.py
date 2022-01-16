from rest_framework import serializers

from core.models import DiscountCode


class DiscountCodesGenerateSerializer(serializers.Serializer):
    number_of_discount_codes = serializers.IntegerField(min_value=1, max_value=1000, required=True)

    def save(self, *args, **kwargs):
        brand_id = kwargs['brand_id']
        number_of_discount_codes = self.data['number_of_discount_codes']
        DiscountCode.create_discount_codes(brand_id, number_of_discount_codes)

        return True
