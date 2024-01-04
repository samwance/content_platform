from django.db import models

from users.models import User

NULL = {'null': True, 'blank': True}


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()
    preview = models.ImageField(upload_to='content_previews/', **NULL)

    def __str__(self):
        return self.name


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, **NULL)
    name = models.CharField()
    description = models.CharField()
    preview = models.ImageField(upload_to='content_previews/', **NULL)
    post_time = models.DateTimeField(auto_now_add=True)
    is_free = models.BooleanField()

    CATEGORY_CHOICES = [
        ('Art', 'Art'),
        ('Poems', 'Poems'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other')
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, default='Other')

    def __str__(self):
        return self.name
