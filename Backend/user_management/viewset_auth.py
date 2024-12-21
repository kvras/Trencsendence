from .models import User
from rest_framework.response import Response # for the response class
from rest_framework.decorators import api_view, permission_classes # for the api_view decorators (eg: @api_view(['GET']))
from django.shortcuts import get_object_or_404

from rest_framework import status
from django.contrib.auth.hashers import check_password # for the password hashing

from datetime import datetime
from django.conf import settings
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


class authViewSet:

    @api_view(['POST'])
    def userLogin(request):
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return Response({"error": "one field or more are missing."}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(User, username=username)
        user.pass_to_2fa = False
        if not check_password(encoded=user.password, password=request.data["password"]):
            return Response({"error": "wrong account credentials."}, status=status.HTTP_400_BAD_REQUEST)

        if user.two_factor_secret != None:
            user.pass_to_2fa = True
            user.save()
            return Response({"success": "verify OTP."}, status=status.HTTP_301_MOVED_PERMANENTLY)

        return generate_login_response(user)


########################

    @api_view(['GET']) ## This could be handled in the frontend only
    @permission_classes([IsAuthenticated])
    def userLogout(request):
        response = Response(status=status.HTTP_200_OK, data={"success": "You logged out successfully."})
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response

########################

    @api_view(['GET'])
    def OAuth(request):
        code = request.GET.get('code')
        if not code:
            return Response({'error': 'Authorization code is not provided.'}, status=status.HTTP_400_BAD_REQUEST)
        
        TOKEN_URL = 'https://user_management.intra.42.fr/oauth/token'
        USER_INFO_URL = 'https://user_management.intra.42.fr/v2/me'

        reqBody = {
            'client_id': settings.OAUTH_CLIENT_ID,
            'client_secret': settings.OAUTH_CLIENT_SECRET,
            'code': code,
            'redirect_uri': settings.OAUTH_REDIRECT_URI,
            'grant_type': 'authorization_code',
        }

        res = requests.post(url=TOKEN_URL, data=reqBody)
        clientToken = res.json().get('access_token')
        if res.status_code != 200 or not clientToken:
            return Response({'error': 'Failed to fetch client access token from 42.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        res = requests.get(
            url=USER_INFO_URL,
            headers={
                'Authorization': f'Bearer {clientToken}',
            }
        )
        clientInfo = res.json()
        if res.status_code != 200:
            return Response({'error': 'Failed to fetch client data from 42.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        login = clientInfo.get('login')
        email = clientInfo.get('email')

        user, isCreated = User.objects.get_or_create(username=login, email=email, password=None)
        return generate_login_response(user)

#########################

def generate_login_response(user):
    # refreshToken = RefreshToken.for_user(user)
    accessToken = RefreshToken.for_user(user).access_token
    response = Response(status=status.HTTP_200_OK, data={"success": "You logged in successfully."})
    
    access_token_expiry = datetime.now() + settings.JWT_ACCESS_EXPIRATION_TIME
    # refresh_token_expiry = datetime.now() + settings.JWT_REFRESH_EXPIRATION_TIME

    response.set_cookie(
    key="access_token",  # The name of the cookie
    value=accessToken,   # The JWT token value
    expires=access_token_expiry,  # Or max_age=3600 if you prefer that
    httponly=True,        # Ensures the cookie is not accessible via JavaScript
    secure=True,          # Set to True for HTTPS (False for HTTP in dev only)
    samesite='Strict',    # Optional: Restrict cross-site cookie sending (can be 'Lax', 'Strict', or None)
    path='/',             # Path where the cookie is available, set to '/' to make it available across the site
)
    # response.set_cookie(
    #     key="refresh_token",
    #     value=refreshToken,
    #     httponly=True,
    #     expires=refresh_token_expiry,
    # )
    return response
