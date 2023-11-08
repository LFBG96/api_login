from django.urls import path
from .views import CreateUserView, LoginUserView,A,UsersViewSet

urlpatterns = [
    path('create/',CreateUserView.as_view()),
    path('login/',LoginUserView.as_view()),
    path('a/',A.as_view()),
    path('users/',UsersViewSet.as_view({'get':'list'})),
    path('user/<int:pk>', UsersViewSet.as_view({'get':'retrieve'})),
    
]