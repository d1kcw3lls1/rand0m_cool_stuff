from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Customer, DiscountCode
from .serializers import DiscountCodesGenerateSerializer


class DiscountCodesGenerateView(GenericAPIView):
    """
    This endpoint generates a number of discount codes for a brand.
    Each discount code can be used once with one user.
    """

    allowed_methods = ('POST', 'OPTIONS', 'HEAD')
    serializer_class = DiscountCodesGenerateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(brand_id=kwargs['pk'])

        return Response({'detail': 'Discount codes generated successfully.'}, status=status.HTTP_201_CREATED)


class DiscountCodeObtainView(APIView):
    """
    This endpoint obtains a discount code from a brand.
    The user is defined by the session/token.
    """

    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        brand_id = kwargs['pk']
        customer_id = request.user.id
        customer_exists = Customer.objects.filter(user_id=customer_id).exists()
        if not customer_exists:
            return Response({'details': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        discount_code = DiscountCode.obtain_discount_code(brand_id, customer_id)

        return Response({'discount_code': discount_code}, status=status.HTTP_200_OK)
