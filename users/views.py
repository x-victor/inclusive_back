from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from users.models import User
from users.serializers import UserSelfSerializer, UserAuthSerializer


class UserSelfViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSelfSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[permissions.AllowAny],
        serializer_class=UserAuthSerializer,
    )
    def auth(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data["email"]
        password = "1234"  # TODO: generate random password
        if user := User.objects.filter(email=email).first():
            user.set_password(password)
            user.save()
        else:
            User.objects.create_user(
                email=email,
                username=email,
                password=password,
            )
        # TODO: send password to email
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(
        detail=False,
        methods=["patch", "get"],
        serializer_class=UserSelfSerializer,
    )
    def me(self, request):
        if request.method == "GET":
            serializer = UserSelfSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = UserSelfSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
