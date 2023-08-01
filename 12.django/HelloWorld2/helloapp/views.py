from django.shortcuts import render
from django.http import HttpResponse
from .models import Message


def hello_world(request):
    return HttpResponse("hello world")

def show_messages(request):
    # DB에서 message 받아오기 ORM 사용해서
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})