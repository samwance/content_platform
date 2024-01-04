from django.db import models

from content.models import NULL
from users.models import User


class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='payer', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2, **NULL)