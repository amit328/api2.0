from django.urls import path

from .views import Listtodo,Detailtodo

urlpatterns=[
    path('',Listtodo.as_view()),
    path('<int:pk>/',Detailtodo.as_view()),
]