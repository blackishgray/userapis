from rest_framework import serializers
from .models import UserApiModel

# serializer for user model
class UserApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserApiModel
        fields = '__all__'
