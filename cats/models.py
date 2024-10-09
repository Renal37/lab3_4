from django.db import models


class CatImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cats/')

    def __str__(self):
        return self.title
