from django.db import models


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateField(auto_now_add=True)