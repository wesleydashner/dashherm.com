from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    user_id = request.POST.get('user_id', 'default_user_id')
    time = request.POST.get('time', 'default_time')
    return JsonResponse({'did_reserve': False})
