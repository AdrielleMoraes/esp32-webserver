from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User
from django.template import loader


def index(request):
    user_list = User.objects.all()
    print(user_list)
    output = ', '.join([user.name for user in user_list])
    context = {
        'user_list': user_list,
    }

    return render(request, 'index.html', context)