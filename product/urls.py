from django.urls import path
from . import views
#"views" is generic name, so type "from"

urlpatterns = [
    path("", views.index)
]