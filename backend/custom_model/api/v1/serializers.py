from rest_framework import serializers
from custom_model.models import CustomModel


class CustomModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomModel
        fields = "__all__"
