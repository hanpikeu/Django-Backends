import uuid

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    discord_id = models.BigIntegerField()
    is_able = models.BooleanField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    token = models.UUIDField(default=uuid.uuid1)
    token_create_time = models.DateTimeField()

    class Meta:
        db_table = 'accounts'
        unique_together = ['discord_id']
