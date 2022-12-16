from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class TodoAPIList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
