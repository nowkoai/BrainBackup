from django.db import models
from django.utils import timezone


class InputText(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.text
