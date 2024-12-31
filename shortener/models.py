from django.db import models
from .utils import generate_short_url

# Create your models here.

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = generate_short_url()
        super().save(*args, **kwargs)
