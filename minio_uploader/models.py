from django.db import models


class Media(models.Model):
    bucket = models.CharField(max_length=256)
    media_saved_name = models.CharField(max_length=256)
    media = models.FileField(upload_to="")
