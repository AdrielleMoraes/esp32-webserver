from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    creat_date = models.DateTimeField('date created')
    def __str__(self):
        return "Username: " + self.name

class Esp32(models.Model):

    distance = models.IntegerField()
    led = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Status: " + self.led