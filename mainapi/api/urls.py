from django.urls import path
from .views import TodoDetailView, TodoListView

urlpatterns = [
    path('', TodoListView.as_view()),
    path('<pk>', TodoDetailView.as_view())
]
