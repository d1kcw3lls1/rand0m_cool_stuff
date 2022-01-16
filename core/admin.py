from django.contrib import admin

from core.models import Brand, Customer, CustomerDiscountCode, DiscountCode


class DiscountCodeAdmin(admin.ModelAdmin):
    search_fields = ['brand__name', 'code']
    list_filter = ['valid']


class CustomerDiscountCodeAdmin(admin.ModelAdmin):
    search_fields = ['customer__email', 'discount_code__brand__name', 'discount_code__code']


admin.site.register(Brand)
admin.site.register(Customer)
admin.site.register(DiscountCode, DiscountCodeAdmin)
admin.site.register(CustomerDiscountCode, CustomerDiscountCodeAdmin)
