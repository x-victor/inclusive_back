from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from users.views import UserSelfViewSet

router = routers.DefaultRouter()
router.register(r"self", UserSelfViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("self/login", views.obtain_auth_token),
]
