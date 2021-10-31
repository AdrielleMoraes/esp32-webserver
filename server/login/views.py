from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from  .models import User
from .mqtt.mqtt_handler import mqtt_client

MQTT_USERNAME = "anmoraes"
MQTT_API = "aio_grMq130grKKPrYmjScmqVXCHMLNV"
MQTT_TOPIC_STATE = MQTT_USERNAME+"/feeds/boiler-control"
MQTT_TOPIC_TEMP = MQTT_USERNAME+"/feeds/temperature"
MQTT_BROKER = "io.adafruit.com"
MQTT_PORT = 1883

# Create your views here.
def index(request):
    user_list = User.objects.order_by('-name')[:5]
    context = {'user_list': user_list}
    return render(request, 'users/index.html', context)


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {'user': user}
    return render(request, 'users/detail.html', context)

def connectMqtt():
    connect_mqtt()

# def results(request, user_id):
#     response = "You're looking at the results of user %s."
#     return HttpResponse(response % user_id)

# def vote(request, user_id):
#     return HttpResponse("You're voting on user %s." % user_id)