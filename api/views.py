from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import CreateUserSerializer, LoginUserSerializer

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
