from django import views
from django.urls import path
from .views import (
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView
)

urlpatterns = [
    path("", ProductListView.as_view()),
    path("add_products/", ProductCreateView.as_view()),
    path("update__product/<pk>/", ProductUpdateView.as_view()),
    path("view__product/<pk>/", ProductDetailView.as_view()),
    path("remove__product/<pk>/", ProductDeleteView.as_view()),

]
