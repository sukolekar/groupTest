from django.db import models


class MultiImage(models.Model):
    photo = models.ImageField(upload_to="multi_box")
    date = models.DateTimeField(auto_now_add=True)
