from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from general_manager import GeneralManager


@csrf_exempt
def index(request):
    lot_id = request.POST.get('lot_id')
    user_id = request.POST.get('user_id')
    if not lot_id or not user_id:
        return get_json_response(False)
    return get_json_response(GeneralManager.make_reservation(lot_id, user_id))


def get_json_response(did_reserve):
    return JsonResponse({'did_reserve': did_reserve})
