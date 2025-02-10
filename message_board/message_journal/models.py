from django.db import models
from django.conf import settings
from django.utils import timezone


class MessagePost(models.Model):
    date = models.DateTimeField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return "{}: {}...".format(self.date, self.text[:100])
