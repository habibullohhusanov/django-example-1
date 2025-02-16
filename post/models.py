from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image_url = models.URLField()
    image = models.ImageField(upload_to='images', default="fallback.png", blank=True)
