
from rest_framework import routers
from .views import TodolistViewset

router = routers.DefaultRouter()
router.register('todos', TodolistViewset, 'todolist')

urlpatterns = router.urls