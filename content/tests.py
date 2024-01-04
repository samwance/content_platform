import datetime

from django.test import TestCase, Client

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from content.models import Content
from subscription.models import Subscription

from users.models import User


class TestContentViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(
            email="user@user.com",
            phone="12345678",
            name="user",
            password="12345",
        )
        self.paid_content = Content.objects.create(
            user=self.user,
            name="test",
            description="test",
            is_free=False,
            post_time=datetime.date.today(),
        )

        self.sub = Subscription.objects.create(
            user=self.user,
            is_active=True,
        )
        self.client.force_login(self.user)
        self.list_url = reverse("content:index")
        self.paid_list_url = reverse("content:paid_content")
        self.detail_url = reverse(
            "content:content_detail", kwargs={"pk": self.paid_content.pk}
        )
        self.delete_url = reverse(
            "content:content_delete", kwargs={"pk": self.paid_content.pk}
        )
        self.create_url = reverse("content:content_create")

    def test_content_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "content/index.html")

    def test_content_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "content/content_detail.html")

    def test_content_delete(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_content_create(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Content.objects.all().count(), 1)
        self.assertEqual(self.paid_content.name, "test")

    def test_paid_content_list(self):
        response = self.client.get(self.paid_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "content/paid_content_list.html")
