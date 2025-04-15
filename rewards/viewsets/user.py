from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rewards.serializers import UserSerializer


class UserViewSet(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение информации о текущем пользователе.",
        responses={
            200: openapi.Response(
                description="Информация о пользователе",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'username': openapi.Schema(type=openapi.TYPE_STRING, description='Имя пользователя'),
                        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email пользователя'),
                        'coins': openapi.Schema(type=openapi.TYPE_INTEGER, description='Количество монет у пользователя'),
                    }
                ),
            ),
            401: openapi.Response(
                description="Пользователь не авторизован"
            ),
        }
    )
    def get(self, request, *args, **kwargs):
        user = request.user
        data = UserSerializer(user).data
        return Response(data, status=status.HTTP_200_OK)
