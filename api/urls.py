from django.urls import path
from views import CreateUserView,
LoginUserView

urlpatterns = [

  path('create/',CreateUserView.as_view()),

  path('login/',LoginUserView.as_view()),
]
