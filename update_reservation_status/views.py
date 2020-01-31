from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from general_manager import GeneralManager
import json


@csrf_exempt
def index(request):
    data = json.loads(request.body.decode('utf-8'))
    lot_id = data.get('lot_id')
    user_id = data.get('user_id')
    status = data.get('status')
    if not lot_id or not user_id or not status:
        return get_json_response(False)
    return get_json_response(GeneralManager.update_reservation_status(lot_id, user_id, status))


def get_json_response(did_update):
    return JsonResponse({'did_update': did_update})
