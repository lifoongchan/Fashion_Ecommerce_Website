from django.urls import path
from . import logview

urlpatterns = [
    path("", logview.login)
]

