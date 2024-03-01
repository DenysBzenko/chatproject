import requests
from django.http import JsonResponse
from medic.settings import NODE_ENDPOINT

def redirect_GET_req_to_express(request):
    try:
        response = requests.get(NODE_ENDPOINT)
        print(response)
        try:
            result = response.json()
            return JsonResponse(result)
        except ValueError:
            print("Raw Response Content:", response.content.decode())
            return JsonResponse({'error': 'Invalid JSON response from Node.js'}, status=500)
    except Exception as e:
        return JsonResponse({'error': f'Error during GET request: {str(e)}'}, status=500)
