from django.shortcuts import render
from django.db.models import Max
from json import loads
from .models import MessagePost
from django.http import HttpResponseBadRequest, HttpResponse


class BadRequestException(Exception):
    pass


def message_overview(request):
    messages = MessagePost.objects.all()
    print(messages)
    #.annotate(latest_post=Max('posts__date')).order_by('-latest_post')
    return render(request, 'message_journal/overview.html', context={
        "messages": [{"text": m.text}
                     for m in messages]
    })


def get_or_make_post(data):
    post = MessagePost(text="")
    print(data)
    if data["text"]:
        text = data["text"]
        post.text = text
    return post


def create_post(request):
    data = loads(request.body)
    post = get_or_make_post(data)
    post.save()
    return HttpResponse("OK")
