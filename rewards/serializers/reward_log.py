from rest_framework import serializers

from rewards.models import RewardLog


class RewardLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = RewardLog
        fields = ['amount', 'given_at', 'requested_by_user']
