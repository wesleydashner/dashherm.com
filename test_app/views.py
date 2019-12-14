from django.http import JsonResponse


def index(request):
    param = request.GET.get('param', 'default')
    return JsonResponse({'param': param})
