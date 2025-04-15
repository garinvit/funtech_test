from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken

class TokenVerifyView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(
        operation_description="Verify the validity of a JWT token.",
        responses={
            200: openapi.Response(
                description="Token is valid.",
                examples={"application/json": {"detail": "Token is valid."}},
            ),
            400: openapi.Response(
                description="Token is required.",
                examples={"application/json": {"detail": "Token is required."}},
            ),
            401: openapi.Response(
                description="Invalid or expired token.",
                examples={"application/json": {"detail": "Token is invalid or expired."}},
            ),
        },
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING, description='JWT token to verify'),
            },
            required=['token'],
        ),
    )
    def post(self, request):
        token = request.data.get('token', None)
        if not token:
            return Response({'detail': 'Token is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            access_token = AccessToken(token)
            return Response({'detail': 'Token is valid.'}, status=status.HTTP_200_OK)
        except InvalidToken:
            return Response({'detail': 'Token is invalid or expired.'}, status=status.HTTP_401_UNAUTHORIZED)