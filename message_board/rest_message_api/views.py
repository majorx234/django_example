from json import loads, decoder
from django.http import HttpResponse
from django.urls import reverse
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
    csrf_token = get_token()
    response = post(settings.DOMAIN + reverse("create_post"), headers={
        "Connection": "Keep-Alive",
        "X-CSRFToken": csrf_token
    }, cookies={
        "csrftoken": csrf_token
    }, json=update_data)
    if response.text != "OK":
        print(response.text)
    return HttpResponse("OK")
