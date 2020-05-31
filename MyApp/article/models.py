from django.db import models


# Create your models here.

class articleInfo(models.Model):
    title = models.CharField(max_length=100, default="")
    content = models.CharField(max_length=1000, default="")
    comment = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.title
