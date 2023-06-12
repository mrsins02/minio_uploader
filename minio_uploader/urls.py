from django.urls import path
from .views import MinioUplaodView

urlpatterns = [
    path("", MinioUplaodView.as_view(), name="home"),
]
