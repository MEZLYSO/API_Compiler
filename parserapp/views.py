from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

# Reuse run_code from parserapp.utils
from .utils import run_code


def index(request):
    # simple form for manual testing
    if request.method == 'GET':
        return render(request, 'parserapp/index.html')
    return JsonResponse({'detail': 'Use POST with JSON {"text": "..."}'}, status=400)


@csrf_exempt
def run(request):
    if request.method != 'POST':
        return JsonResponse({'code': ''}, status=405)
    try:
        body = request.body.decode('utf-8') if request.body else ''
        data = json.loads(body) if body else {}
    except Exception:
        return JsonResponse({'code': 'Invalid JSON'}, status=400)
    code = data.get('text', '')
    success, output = run_code(code)
    # Always return the parser output or the traceback/error as the value for 'code'
    return JsonResponse({'code': output})
