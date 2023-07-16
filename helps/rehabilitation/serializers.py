from rest_framework import serializers

from helps.rehabilitation.models import RehabilitationCenter


class RehabilitationCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RehabilitationCenter
        fields = "__all__"
