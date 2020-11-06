from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from todos import models
from .serializers import Todoserializers

class Listtodo(generics.ListCreateAPIView):
    queryset=models.Todo.objects.all()
    serializer_class=Todoserializers


class Detailtodo(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Todo.objects.all()
    serializer_class=Todoserializers