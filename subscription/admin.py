from django.contrib import admin

from subscription.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("__str__",)
