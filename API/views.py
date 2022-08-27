from rest_framework import generics, permissions, viewsets, renderers
from .models import Todolist
from API.serializers import TodolistSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# class TodolistViewset(viewsets.ModelViewSet):
#     serializer_class = TodolistSerializer
#     permission_classes = [
#         permissions.AllowAny
#     ]


#     def get_queryset(self):
#         return self.request.user.todolist.all()

#     def perform_create(self, serializer):
#         serializer.save(task_manager = self.request.user)

    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     todolist = self.get_object()
    #     return Response(todolist.highlighted)


class TodolistListAPIView(generics.ListAPIView):
    serializer_class = TodolistSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    # queryset = Todolist.objects.all()

    def get_queryset(self):
        return self.request.user.todolist.all()

    


class TodolistDetailAPIView(generics.RetrieveAPIView):
    serializer_class = TodolistSerializer
    queryset = Todolist.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    


class TodolistCreateAPIView(generics.CreateAPIView):
    serializer_class = TodolistSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = Todolist.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(task_manager = self.request.user)


class TodolistUpdateAPIView(generics.UpdateAPIView):
    serializer_class = TodolistSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Todolist.objects.all()


class TodolistDeleteAPIView(generics.DestroyAPIView):
    serializer_class = TodolistSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    queryset = Todolist.objects.all()



