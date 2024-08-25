# firebase_test/views.py

from firebase_admin import auth
from django.http import JsonResponse, HttpResponse  # Import HttpResponse here

def test_firebase(request):
    try:
        # A simple call to Firebase to test the connection
        users = auth.list_users().users
        return JsonResponse({"status": "success", "user_count": len(users)})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)

def home(request):
    return HttpResponse("Welcome to Snake2 Home Page!")
