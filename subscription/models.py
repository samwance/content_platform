from django.db import models

from content.models import NULL
from users.models import User


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name="payer", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
