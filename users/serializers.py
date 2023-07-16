from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager

from users.models import User


class UserSelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "username",
            "email",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "about",
        ]
        read_only_fields = ["uuid", "username", "email"]


class UserAuthSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        email = BaseUserManager.normalize_email(email)
        return email
