from rest_framework import generics, permissions, viewsets
from .models import Todolist
from API.serializers import TodolistSerializer


class TodolistViewset(viewsets.ModelViewSet):
    serializer_class = TodolistSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]


    def get_queryset(self):
        return self.request.user.todolist.all()

    def perform_create(self, serializer):
        serializer.save(task_manager = self.request.user)

