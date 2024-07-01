import requests
from django.http import JsonResponse
from django.utils import timezone

def hello_api(request):
    visitor_name = request.GET.get('visitor_name', 'Mark')
    client_ip = request.META.get('REMOTE_ADDR')
    geolocation_api_key = "632b759811ba4551b28621a0cd96b7eb"
    weather_api_key = "30d3ed10ba347bfeaf1a468b825f6b83"
    
    try:
        geolocation_url = f"https://api.ipgeolocation.io/ipgeo?apiKey={geolocation_api_key}&ip={client_ip}"
        geolocation_response = requests.get(geolocation_url)
        geolocation_data = geolocation_response.json()
        city = geolocation_data.get("city", "Lagos")
    except requests.RequestException as e:
        print(f"Geolocation API request failed: {e}")
        city = "Lagos"
    
    try:
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric"
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        if weather_data.get('cod') == 200:
            temperature = weather_data['main']['temp']
        else:
            temperature = None
    except requests.RequestException as e:
        print(f"Weather API request failed: {e}")
        temperature = None
    
    location = city
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}" if temperature else f"Hello, {visitor_name}! The temperature data is unavailable for {location}"
    response_data = {
        'client_ip': client_ip,
        'location': city,
        'greeting': greeting,
        'server_time': timezone.now().isoformat()
    }
    
    return JsonResponse(response_data)
