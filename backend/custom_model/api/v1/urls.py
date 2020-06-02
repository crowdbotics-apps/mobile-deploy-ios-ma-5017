from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomModelViewSet

router = DefaultRouter()
router.register("custommodel", CustomModelViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
