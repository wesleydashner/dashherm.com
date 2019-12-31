from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from general_manager import GeneralManager
import json


@csrf_exempt
def index(request):
    # these should be PUT's, but django doesn't support PUT
    data = json.loads(request.body.decode('utf-8'))
    lot_id = data.get('lot_id')
    statuses = data.get('statuses')
    if not lot_id or not statuses:
        return get_json_response(False)
    return get_json_response(GeneralManager.update_stalls(lot_id, statuses))


def get_json_response(did_update):
    return JsonResponse({'did_update': did_update})
