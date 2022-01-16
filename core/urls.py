from django.urls import path

from core import views

urlpatterns = [
    path(
        'brands/<int:pk>/generate-discount-codes/',
        views.DiscountCodesGenerateView.as_view(),
        name='discount_codes_generate',
    ),
    path('brands/<int:pk>/obtain-discount-code/', views.DiscountCodeObtainView.as_view(), name='discount_code_obtain'),
]
