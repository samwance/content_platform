import datetime

from django.test import TestCase, Client

from django.urls import reverse

from content.models import Content, Collection

from users.models import User


class TestContentViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(
            phone="12345678", name="user", password="12345", is_subscribed=True
        )
        self.collection = Collection.objects.create(
            user=self.user,
            name="test",
            description="test",
        )
        self.paid_content = Content.objects.create(
            user=self.user,
            name="test",
            description="test",
            is_free=False,
            post_time=datetime.date.today(),
            collection=self.collection,
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
        # Create an existing object
        existing_content = Content.objects.create(
            user=self.user,
            name="test",
            description="test",
            is_free=False,
            post_time=datetime.date.today(),
            collection=self.collection,
        )

        # Log in the client
        self.client.force_login(self.user)

        # Send a POST request to create a new object
        response = self.client.post(self.create_url)

        # Check that the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check that the number of objects in the database is 2
        self.assertEqual(Content.objects.all().count(), 2)

        # Check that the name of the existing object is "existing"
        self.assertEqual(existing_content.name, "test")

    def test_paid_content_list(self):
        response = self.client.get(self.paid_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "content/paid_content_list.html")


class TestCollectionViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.user = User.objects.create(
            phone="12345678",
            name="user",
            password="12345",
        )
        self.collection = Collection.objects.create(
            user=self.user,
            name="test",
            description="test",
        )
        self.client.force_login(self.user)
        self.list_url = reverse("content:collection_list")
        self.detail_url = reverse(
            "content:collection_detail", kwargs={"pk": self.collection.pk}
        )
        self.delete_url = reverse(
            "content:collection_delete", kwargs={"pk": self.collection.pk}
        )
        self.create_url = reverse("content:collection_create")

    def test_collection_list(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "content/collection_list.html")

    def test_collection_detail(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "content/collection_detail.html")

    def test_collection_delete(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_collection_create(self):
        response = self.client.post(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Collection.objects.all().count(), 1)
        self.assertEqual(self.collection.name, "test")
