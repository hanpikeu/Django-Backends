import uuid

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    discord_name = models.CharField(max_length=32)
    discord_id = models.BigIntegerField()
    is_able = models.BooleanField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    token = models.UUIDField(default=uuid.uuid1, null=True)
    token_create_time = models.DateTimeField(null=True)

    def __str__(self):
        text = "Account " + str(self.discord_name)
        if not self.is_able:
            text += ' - {is blocked} '
        text += ' - ' + str(self.token_create_time)
        return text

    class Meta:
        db_table = 'accounts'
        unique_together = ['discord_id']
