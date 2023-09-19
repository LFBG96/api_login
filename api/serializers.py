from rest_framework import serializers
from django.contrib.auth.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password',)
    def create(self,validade_data):
        username = validade_data.get("username")
        password = validade_data.get("password")
        user = User.objects.create(
            username=username,
            password=password,
        )
        user.set_password(password)
        user.save()
        return user

class LoginUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ('username','password')

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password") 
        user = User.objects.filter(username=username).first()
        if not user:
            raise serializers.ValidationError({"username":"Usuario invalido"})
        if not user.check_password(password):
            raise serializers.ValidationError({"password":"Senha invalida"})
            
        return super().validate(attrs)

    def create(self,validate_data):
        username = validate_data.get("username")
        user = User.objects.filter(username=username).first()
        return user