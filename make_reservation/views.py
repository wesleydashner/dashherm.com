from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from general_manager import GeneralManager
from datetime import datetime


@csrf_exempt
def index(request):
    lot_id = request.POST.get('lot_id')
    user_id = request.POST.get('user_id')
    time = str(datetime.utcnow())
    if not lot_id or not user_id or not time:
        print('something missing')
        return JsonResponse({'did_reserve': False})
    return JsonResponse({'did_reserve:': GeneralManager.make_reservation(lot_id, user_id, time)})
