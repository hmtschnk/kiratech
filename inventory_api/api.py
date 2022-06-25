from rest_framework.serializers import ModelSerializer
from inventory.models import inventory

class inv_serializer(ModelSerializer):
    class Meta:
        model = inventory
        fields = (
            "id",
            "name",
            "supplier",
        )