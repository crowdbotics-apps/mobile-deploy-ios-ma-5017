from rest_framework import authentication
from custom_model.models import CustomModel
from .serializers import CustomModelSerializer
from rest_framework import viewsets


class CustomModelViewSet(viewsets.ModelViewSet):
    serializer_class = CustomModelSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomModel.objects.all()
