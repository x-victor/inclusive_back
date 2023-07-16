from django.urls import path, include
from rest_framework.routers import DefaultRouter

from helps.rehabilitation.views import RehabilitationCenterViewSet

router = DefaultRouter()

router.register(r"rehabilitation_centers", RehabilitationCenterViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
