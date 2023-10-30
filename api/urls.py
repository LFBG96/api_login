from django.urls import path
from .views import CreateUserView, LoginUserView,A

urlpatterns = [
    path('create/',CreateUserView.as_view()),
    path('login/',LoginUserView.as_view()),
    path('a/',A.as_view()),
    
]