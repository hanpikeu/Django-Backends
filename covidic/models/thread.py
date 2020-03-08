from django.db import models

from account_manager.models.account import Account


class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)

    create_user = models.ForeignKey(
        'account_manager.Account',
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'threads'
