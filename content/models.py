from django.db import models

from users.models import User

NULL = {"null": True, "blank": True}


class Collection(models.Model):
    user = models.ForeignKey(
        User, related_name="collection_user", on_delete=models.CASCADE
    )
    name = models.CharField()
    description = models.TextField(**NULL)
    preview = models.ImageField(upload_to="collection_previews/", **NULL)

    def __str__(self):
        return self.name


class Content(models.Model):
    user = models.ForeignKey(
        User, related_name="content_user", on_delete=models.CASCADE
    )
    name = models.CharField()
    description = models.TextField()
    preview = models.ImageField(upload_to="content_previews/", **NULL)
    post_time = models.DateTimeField(auto_now_add=True)
    is_free = models.BooleanField()
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, **NULL)

    CATEGORY_CHOICES = [
        ("Art", "Art"),
        ("Poems", "Poems"),
        ("Education", "Education"),
        ("Entertainment", "Entertainment"),
        ("Not_selected", "Not selected"),
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, default="Not selected")

    def __str__(self):
        return self.name
