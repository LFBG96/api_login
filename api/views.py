from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.status import HTTP_200_OK,HTTP_403_FORBIDDEN
from django.utils import timezone
from .models import User
from rest_framework import viewsets


from .serializers import CreateUserSerializer,LoginUserSerializer,UserSerializer

class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
  
        if serializer.is_valid():
            user = serializer.save()
            
            serializer_data = serializer.data
            print(user.id)
            serializer_data.update(dict(timestamp=timezone.now(),id=user.id))
            return Response(serializer_data)
        
        
      
        return super().create(request, *args, **kwargs)
    
class LoginUserView(CreateAPIView):
    serializer_class = LoginUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)   
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(dict(
                userAuth="true",
                id=user.id,
                cep=user.cep,
                username=user.username,
                client_code=user.client_code,
                #refresh=str(refresh),
                token_type= "Bearer",
                token=str(refresh.access_token),
                timestamp=timezone.now()

            ),status=HTTP_200_OK
            )
            

        return Response(serializer.errors,status=HTTP_403_FORBIDDEN)
    

class A(ListAPIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [JWTAuthentication,]
    def list(self,request):
        return Response(dict(
            mensagem="Token válido",
            fato="LOL>Dota",
            timestamp=timezone.now()
        ))

class UsersViewSet(viewsets.ViewSet):
    #permission_classes = [IsAuthenticated,]
    #authentication_classes = [JWTAuthentication,]
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        print(serializer)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, client_code=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

