from django.db import models

from users.models import User

NULL = {'null': True, 'blank': True}



class Content:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.CharField()
    preview = models.ImageField(upload_to='content_previews/', **NULL)
    video_file = models.FileField(upload_to='video/', **NULL)
    audio_file = models.FileField(upload_to='audio/', **NULL)
    is_free = models.BooleanField()
    price = models.DecimalField(decimal_places=2, **NULL)

    CATEGORY_CHOICES = [
        ('Art', 'Art'),
        ('Music', 'Music'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('Literature', 'Literature'),
        ('Not_selected', 'Not selected')
    ]
    category = models.CharField(choices=CATEGORY_CHOICES, default='Not_selected')
