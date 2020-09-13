from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default="no")
    age = models.IntegerField(null=False, default=13)

    def __str__(self):
        return self.name