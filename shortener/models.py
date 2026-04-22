from django.db import models

# Create your models here.

class URL(models.Model):
    original_Url = models.URLField()
    short_code = models.CharField(max_length=7, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.original_Url