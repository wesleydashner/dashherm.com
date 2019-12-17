from django.http import JsonResponse


def index(request):
    return JsonResponse({'available_stalls_count': -1})
