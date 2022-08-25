
from rest_framework import routers
# from .views import TodolistViewset

# router = routers.DefaultRouter()
# router.register('todos', TodolistViewset, 'todolist')

# urlpatterns = router.urls


# newwwwwwwwwwwwwww



from django.urls import path
from .views import *

urlpatterns = [
    path("todos/", TodolistListAPIView.as_view()),
    path("view_task/<pk>/", TodolistDetailAPIView.as_view()),
    path("add_new_task/", TodolistCreateAPIView.as_view()),
    path("edit_task/<pk>/", TodolistUpdateAPIView.as_view()),
    path("delete_task/<pk>/", TodolistDeleteAPIView.as_view()),
]
