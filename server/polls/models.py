from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name

class Esp32(models.Model):

    distance = models.IntegerField()
    led = models.BooleanField()
    owner = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Status: " + self.led