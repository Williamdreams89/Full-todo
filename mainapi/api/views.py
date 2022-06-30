from rest_framework.generics import ListAPIView, RetrieveAPIView
from mainapi.models import Todo
from .serializers import TodoSerializer


class TodoListView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer