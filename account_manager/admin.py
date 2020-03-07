from django.contrib import admin

from .models import *

@admin.register(Account)
class Admin_Account(admin.ModelAdmin):
    readonly_fields = [
        'account_id',
        'created_time',
        'modified_time',
    ]
