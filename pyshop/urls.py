from django.contrib import admin
from django.urls import path, include
from . import mainview

urlpatterns = [
    path('admin/', admin.site.urls),
    path("product/", include("product.urls")),
    path("main/", mainview.index),
    path("login/", include("login.urls"))
]
