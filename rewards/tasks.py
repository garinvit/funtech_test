from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from app.celery import app
from .models import ScheduledReward, RewardLog

@shared_task
def process_scheduled_rewards():
    rewards = ScheduledReward.objects.filter(execute_at__lte=now())
    reward_logs = list()
    for reward in rewards:
        reward.user.coins += reward.amount
        reward.user.save()
        reward_logs.append(RewardLog(user=reward.user, amount=reward.amount, requested_by_user=reward.requested_by_user,))
        reward.delete()
    RewardLog.objects.bulk_create(reward_logs)
    return f"Processed {len(reward_logs)} rewards."

app.conf.beat_schedule = {
    "process_scheduled_rewards": {
        "task": 'rewards.tasks.process_scheduled_rewards',
        "schedule": timedelta(minutes=1),
    },
}