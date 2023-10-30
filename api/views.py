from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from django.utils import timezone



from .serializers import CreateUserSerializer,LoginUserSerializer

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            
            
            serializer_data = serializer.data
            serializer_data.update(dict(timestamp=timezone.now()))
            return Response(serializer_data)
        
        
      
        return super().create(request, *args, **kwargs)
    
class LoginUserView(CreateAPIView):
    serializer_class = LoginUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user) #apagar
            return Response(dict(
                userAuth="true",
                #refresh=str(refresh),
                token=str(refresh.access_token),
                timestamp=timezone.now()

            ),status=HTTP_200_OK
            )
            

        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
    

class A(ListAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]
    def list(self,request):
        return Response(dict(
            mensagem="Token válido",
            fato="LOL>Dota",
            timestamp=timezone.now()
        ))
