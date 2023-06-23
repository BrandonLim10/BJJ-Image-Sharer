from django.db import models
from sorl.thumbnail import ImageField

class Post(models.Model):
    title = models.CharField(max_length=20, blank=False, null=False)
    text = models.TextField(max_length=500, blank=False, null=False)
    image = ImageField()

    def __str__(self) -> str:
        return self.title
