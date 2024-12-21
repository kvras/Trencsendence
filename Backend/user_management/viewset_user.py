from .models import User
from rest_framework.response import Response # for the response class
from rest_framework.decorators import api_view # for the api_view decorators (eg: @api_view(['GET']))
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# for User table
class UserTableViewSet:

    @api_view(['POST'])
    def createUser(request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": serializer.data})

    ######################

    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def getAllUsers(request):
        allUsers = User.objects.all()
        serializer = UserSerializer(instance=allUsers, many=True)
        return Response(serializer.data)

    ########################

    @api_view(['POST'])
    @permission_classes([IsAuthenticated])
    def updateUser(request):
        user = request.user
        serializer = UserSerializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

