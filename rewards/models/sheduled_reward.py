from django.db import models

from rewards.models import User


class ScheduledReward(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scheduled_rewards',
                             verbose_name='Пользователь')
    amount = models.IntegerField('Количество')
    execute_at = models.DateTimeField('Дата выдачи награды')
    requested_by_user = models.BooleanField('Запрошено пользователем', default=False)

    class Meta:
        verbose_name = 'Запланированная награда'
        verbose_name_plural = 'Запланированные награды'

    def __str__(self):
        return f"ScheduledReward(user={self.user.username}, amount={self.amount}, execute_at={self.execute_at}, requested_by_user={self.requested_by_user})"