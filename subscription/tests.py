from django.test import TestCase, Client
from django.urls import reverse

from subscription.models import Subscription
from users.models import User


class TestSubscriptionViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(phone=12345678, name="user")
        self.client.force_login(self.user)
        self.create_url = reverse("subscription:subscribe")
        self.payment = Subscription.objects.create(
            user=self.user,
            is_active=False,
        )

    def test_sub_create(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Subscription.objects.all().count(), 1)
