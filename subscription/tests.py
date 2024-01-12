
from django.test import TestCase, Client

from django.urls import reverse

from subscription.models import Payment
from users.models import User


class TestPaymentViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            phone=12345678, name="User"
        )
        self.client.force_login(self.user)
        self.create_url = reverse("subscription:create-checkout-session")
        self.payment_1 = Payment.objects.create(
            app_user=self.user,
            stripe_checkout_id="test12345",
        )

    def test_payment_create(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Payment.objects.all().count(), 2)