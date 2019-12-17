from django.http import JsonResponse


def index(request):
    return JsonResponse({'did_update': False})
