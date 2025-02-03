from datetime import timedelta
from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse

from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .middleware import authenticated


# i created a user in the data base as a start point
# then each user aka admin can create a another one
@api_view(['POST'])
@authenticated
def register_controller(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        response = JsonResponse({
            "user": serializer.data,
        })
        response.set_cookie(
            'access-token', str(refresh.access_token),
            httponly=True,
            max_age=timedelta(days=7),
            samesite='Strict'
        )
        return response
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login_controller(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({"error": "username and password are required"}, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        response = JsonResponse({
            "message": "Login successful",
            "user": UserSerializer(user).data,
        })
        response.set_cookie(
            'access-token', str(refresh.access_token),
            httponly=True,
            max_age=timedelta(days=7),
            samesite='Strict'
        )
        return response
    return Response({"error": "Invalid credentials"}, status=401)


@api_view(['POST'])
def logout_controller(request):
    response = JsonResponse({"message": "Logout successful"})
    response.delete_cookie('access-token')
    return response