from rest_framework import serializers
#from django.contrib.auth.models import User

from .models import User

from django.utils import timezone
import random

def generate_unique_number():
    number = random.randint(100000, 999999)
    while User.objects.filter(client_code=number).exists():
        number = random.randint(100000, 999999)
    return number

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','cep','client_code')
    
    def create(self,validade_data):
        username = validade_data.get("username")
        password = validade_data.get("password")
        cep = validade_data.get("cep")
    
        user = User.objects.create(
            username=username,
            password=password,
            cep=cep,
            client_code=generate_unique_number()
        )
        
        user.set_password(password)
        user.save()
        return user

class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('username','password',)
   

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password") 
        user = User.objects.filter(username=username).first()
        
        if not user:
            raise serializers.ValidationError({"userAuth":"false","timesamp":timezone.now()})
        if not user.check_password(password):
            raise serializers.ValidationError({"password":"Senha invalida","timesamp":timezone.now()})
            
        
        return super().validate(attrs)

    def create(self,validate_data):
        username = validate_data.get("username")
        user = User.objects.filter(username=username).first()
        return user