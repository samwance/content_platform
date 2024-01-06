from django.contrib.auth.models import AbstractUser
from django.db import models
from image_cropping import ImageCropField


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=35, unique=True)
    name = models.CharField(max_length=100, unique=True)
    photo = ImageCropField(upload_to='users/', null=True, blank=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.name}"
