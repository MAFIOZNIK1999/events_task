from django.contrib.auth import get_user_model
from rest_framework import serializers

MIN_LENGTH_PASSWORD = 5

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": MIN_LENGTH_PASSWORD}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
