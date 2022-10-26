from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from testapi.models import personal_data

class dataSerializer(ModelSerializer):
    class Meta:
        model=personal_data
        fields='__all__'