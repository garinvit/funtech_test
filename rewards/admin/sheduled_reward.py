from django.contrib import admin
from ..models import ScheduledReward


@admin.register(ScheduledReward)
class ScheduledRewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'execute_at', 'requested_by_user')
    search_fields = ('user__username', 'user__email')
    list_filter = ('execute_at',)
    ordering = ('execute_at',)

