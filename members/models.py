from django.db import models
from django.utils import timezone


class Member(models.Model):
    objects = None
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"