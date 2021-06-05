from django.db import models

# Create your models here.
class Client(models.Model):

    name = models.TextField()

class Devices(models.Model):

    name = models.TextField()

    distance = models.IntegerField()

    led = models.BooleanField()

    owner = models.ForeignKey("Client", on_delete=models.SET_NULL, null=True)