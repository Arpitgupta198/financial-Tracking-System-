from rest_framework import serializers
from .models import User
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]

    def create(self,validated_data):
        return User.objects.create(**validated_data)
