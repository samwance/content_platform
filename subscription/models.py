from django.db import models
from users.models import User


class Payment(models.Model):
    app_user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_checkout_id = models.CharField(max_length=500)
