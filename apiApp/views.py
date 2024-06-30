from django.http import JsonResponse
from django.utils import timezone

def hello_api(request):
    visitor_name = request.GET.get('visitor_name', 'World')
    client_ip = request.META.get('REMOTE_ADDRESS')
    location = 'New York'
    greeting = f"Hello, {visitor_name}! The temperature is 11 degrees Celcius in {location}"
    response_data = {
        "client_ip" : client_ip,
        "location" : location,
        "greeting" : greeting,
        "server_time" : timezone.now().isoformat()
    }
    
    return JsonResponse(response_data)