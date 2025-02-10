from json import loads, decoder
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from requests import post
from django.middleware.csrf import get_token

# Create your views here.
def message(request):
    try:
        update_data = loads(request.body)
        print("message request data:")
        print(update_data)
        print("---------------------")
    except decoder.JSONDecodeError:
        return HttpResponse("Error: This is not vaild JSON.", status=500)
    response = post(settings.DOMAIN + reverse("create_post"), headers={
        "Connection": "Keep-Alive"
    }, json=update_data)
    if response.text != "OK":
        print(response.text)
    return HttpResponse("OK")
