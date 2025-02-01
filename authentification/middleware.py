from .models import User
from functools import wraps
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from django.http import JsonResponse

def authenticated(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        access_token = request.COOKIES.get('access-token')
        if not access_token:
            return JsonResponse({"error": "No access token provided"}, status=401)
        try:
            access_token_obj = AccessToken(access_token)
            user_id = access_token_obj['user_id']
            request.user = User.objects.get(id=user_id)
        except Exception as e:
            return JsonResponse({"error": "Invalid or expired access token"}, status=401)

        return view_func(request, *args, **kwargs)
    return _wrapped_view