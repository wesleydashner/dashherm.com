from django.http import JsonResponse
from general_manager import GeneralManager


def index(request):
    lot_id = request.GET.get('lot_id')
    if not lot_id:
        return get_json_response(0)
    return get_json_response(GeneralManager.get_available_stalls_count(lot_id))


def get_json_response(available_stalls_count):
    return JsonResponse({'available_stalls_count': available_stalls_count})
