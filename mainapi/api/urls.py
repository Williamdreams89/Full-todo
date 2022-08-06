from django.urls import path
from .views import TodoCreateView, TodoDeleteView, TodoDetailView, TodoListView, TodoUpdateView

urlpatterns = [
    path('', TodoListView.as_view()),
    path('view_task/<pk>', TodoDetailView.as_view()),
    path('add_new_task/', TodoCreateView.as_view()),
    path('remove_task/<pk>/', TodoDeleteView.as_view()),
    path('edit_task/<pk>/', TodoUpdateView.as_view()),

]
