# views.py
from django.http import JsonResponse
from .models import HelloWorld
from django.views.decorators.csrf import csrf_exempt
import json

# POST API to insert "Hello, World!" into the database
@csrf_exempt
def insert_hello_world(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message', 'default')
            hello_world = HelloWorld.objects.create(message=message)
            return JsonResponse({"message": "Post success!"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

# GET API to fetch "Hello, World!" from the database
def fetch_hello_world(request):
    hello_world = HelloWorld.objects.last()  # Get the latest "HelloWorld" entry
    if hello_world:
        return JsonResponse({"message": hello_world.message}, status=200)
    return JsonResponse({"error": "No data found"}, status=404)
