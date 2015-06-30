from django.db import models

__all__ = ['Image']


class Image(models.Model):
    """Model for representing an Image"""
    image = models.ImageField(null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image
