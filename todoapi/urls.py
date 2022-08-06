
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_api/', include("mainapi.api.urls")),
    path('products_api/', include("products_api.urls")),
    path('main__products_api/', include("products_api.mainapi.urls")),

]
