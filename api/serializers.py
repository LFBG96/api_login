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
