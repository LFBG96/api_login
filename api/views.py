from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import CreateUserSerializer, LoginUserSerializer

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer

class LoginUserView(CreateUserView):
    serializer_class = LoginUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response(dict(
                mensagem="logado com sucesso",
            ),status=HTTP_200_OK
            )
            
        
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    

