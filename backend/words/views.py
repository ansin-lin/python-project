from django.http import JsonResponse
from .models import Word

def words_api(request):
    items = list(Word.objects.values("id", "text", "meaning", "example", "created_at"))
    return JsonResponse({"items": items})
