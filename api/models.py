from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    cep = models.CharField(max_length=9)
    client_code = models.IntegerField(unique=True,default=0)


    def __str__(self) -> str:
        return f"{self.id} - {self.username}"
 