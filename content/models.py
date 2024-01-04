from django.db import models

from users.models import User

NULL = {'null': True, 'blank': True}


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()
    preview = models.ImageField(upload_to='content_previews/', **NULL)


class Content(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()
    preview = models.ImageField(upload_to='content_previews/', **NULL)
    video_file = models.FileField(upload_to='video/', **NULL)
    audio_file = models.FileField(upload_to='audio/', **NULL)
    is_free = models.BooleanField()

    CATEGORY_CHOICES = [
        ('Art', 'Art'),
        ('Music', 'Music'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Literature', 'Literature'),
        ('Not_selected', 'Not selected')
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, default='Not_selected')
