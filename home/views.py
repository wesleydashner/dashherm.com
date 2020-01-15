from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from general_manager import GeneralManager
import json


# @csrf_exempt
def index(request):
    return get_http_response()


def get_http_response():
    r = HttpResponse('welcome to dashherm.com')
    return HttpResponse('welcome to dashherm.com')
