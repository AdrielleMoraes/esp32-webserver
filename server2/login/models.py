from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Esp32(models.Model):

    distance = models.IntegerField()
    led = models.BooleanField()
    owner = models.ManyToManyField(User)

    def __str__(self):
        return 'On' if self.led else'Off'