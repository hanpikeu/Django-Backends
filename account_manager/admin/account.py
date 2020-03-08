from django.contrib import admin

from account_manager.models.account import Account


@admin.register(Account)
class AdminInterfaceAccount(admin.ModelAdmin):
    readonly_fields = [
        'account_id',
        'created_time',
        'modified_time',
    ]
