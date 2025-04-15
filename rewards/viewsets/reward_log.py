from datetime import timedelta

from django.utils import timezone
from django.utils.timezone import localtime, now
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rewards.models import RewardLog, ScheduledReward
from rewards.serializers import RewardLogSerializer


class RewardLogViewSet(viewsets.GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = RewardLogSerializer

    def get_queryset(self):
        return RewardLog.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        """
        Получение списка всех выданных наград текущему пользователю.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    @swagger_auto_schema(
        operation_description="Запрос на награду. Доступно только 1 раз в текущие сутки.",
        responses={
            201: openapi.Response(description="Награда успешно запрошена."),
            400: openapi.Response(description="Награда уже была запрошена сегодня."),
            401: openapi.Response(description="Пользователь не авторизован."),
        },
    )
    def request_reward(self, request, *args, **kwargs):
        user = request.user
        start_of_today = localtime(now()).replace(hour=0, minute=0, second=0, microsecond=0)
        reward_already_requested = (
                RewardLog.objects.filter(user=user, given_at__gte=start_of_today, requested_by_user=True).exists() or
                ScheduledReward.objects.filter(user=user,
                                               execute_at__lte=timezone.now() + timedelta(minutes=5),
                                               requested_by_user=True,).exists()
        )

        if reward_already_requested:
            return Response(
                {"detail": "Вы уже запрашивали награду сегодня."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        ScheduledReward.objects.create(
            user=user,
            amount=1,
            execute_at=timezone.now() + timedelta(minutes=5),
            requested_by_user=True
        )

        return Response(
            {"detail": "Награда успешно запрошена. Она будет начислена через 5 минут."},
            status=status.HTTP_201_CREATED,
        )