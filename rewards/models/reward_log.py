from django.db import models

from rewards.models import User


class RewardLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reward_logs', verbose_name='Пользователь')
    amount = models.IntegerField('Количество')
    given_at = models.DateTimeField('Дата выдачи награды', auto_now=True)
    requested_by_user = models.BooleanField('Запрошено пользователем', default=False)

    class Meta:
        verbose_name = 'Журнал наград'
        verbose_name_plural = 'Журналы наград'

    def __str__(self):
        return f"RewardLog(user={self.user.username}, amount={self.amount}, given_at={self.given_at}, requested_by_user={self.requested_by_user})"