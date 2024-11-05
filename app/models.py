from django.db import models

class Image(models.Model):
    photo = models.ImageField(upload_to="media/")
    date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=True, null=True, )
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.photo.name} - {self.category}"