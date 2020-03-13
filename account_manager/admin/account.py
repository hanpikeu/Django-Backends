from django.contrib import admin

from account_manager.models.account import Account


@admin.register(Account)
class AdminInterfaceAccount(admin.ModelAdmin):
    readonly_fields = ['account_id', 'created_time', 'modified_time', 'token', 'token_create_time']

    list_display = ['account_id', 'discord_id', 'is_able', 'token_create_time']

    fieldsets = (
        ('Main', {
            'fields': ('account_id', 'is_able', 'discord_name', 'discord_id')
        }),
        ('Log', {
            'fields': ('created_time', 'modified_time')
        }),
        ('Token', {
            'fields': ('token', 'token_create_time')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        read_only_fields = ['account_id', 'created_time', 'modified_time', 'token', 'token_create_time']
        if obj is not None:
            read_only_fields.append('discord_id')
        return read_only_fields
