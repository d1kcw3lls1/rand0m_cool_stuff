from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from core.models import Brand, Customer, CustomerDiscountCode, DiscountCode

User = get_user_model()


class DiscountCodeTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user('testuser', '123456')
        self.client.force_authenticate(self.test_user)

    def test_create_discount_code(self):
        brand = Brand(name='Brand A')
        brand.save()

        url = reverse('discount_codes_generate', args=(brand.id,))
        data = {'number_of_discount_codes': '5'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(DiscountCode.objects.count(), 5)

    def test_obtain_discount_code(self):
        customer = Customer(email='customer@email.com')
        customer.save()
        brand = Brand(name='Brand A')
        brand.save()
        DiscountCode.create_discount_codes(brand.id, 5)

        url = reverse('discount_code_obtain', args=(brand.id,))
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(DiscountCode.objects.filter(valid=True).count(), 4)
        self.assertEqual(CustomerDiscountCode.objects.count(), 1)

    def test_obtain_discount_code_customer_not_found(self):
        brand = Brand(name='Brand A')
        brand.save()
        DiscountCode.create_discount_codes(brand.id, 5)

        url = reverse('discount_code_obtain', args=(brand.id,))
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
