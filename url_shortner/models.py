from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Url(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url_id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=10000)
    short_url = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.short_url
