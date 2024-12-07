from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length = 200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



