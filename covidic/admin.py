from django.contrib import admin

from .models import *


@admin.register(Account)
class AdminInterfaceAccount(admin.ModelAdmin):
    readonly_fields = [
        'account_id',
        'created_time',
        'modified_time',
    ]
