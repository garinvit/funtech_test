from django.contrib import admin
from ..models import RewardLog


@admin.register(RewardLog)
class RewardLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'given_at', 'requested_by_user')
    search_fields = ('user__username', 'user__email')
    list_filter = ('given_at',)
    ordering = ('given_at',)

