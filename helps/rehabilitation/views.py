from rest_framework.viewsets import ReadOnlyModelViewSet

from helps.rehabilitation.models import RehabilitationCenter
from helps.rehabilitation.serializers import RehabilitationCenterSerializer


class RehabilitationCenterViewSet(ReadOnlyModelViewSet):
    queryset = RehabilitationCenter.objects.all()
    serializer_class = RehabilitationCenterSerializer
    permission_classes = []
