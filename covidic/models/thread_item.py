from django.db import models


class ThreadItem(models.Model):
    thread_item_id = models.AutoField(primary_key=True)

    create_user = models.ForeignKey(
        'account_manager.Account',
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
        editable=False
    )
    content = models.ForeignKey(
        'Archive',
        on_delete=models.PROTECT,
        related_name='references'
    )
    parent_thread = models.ForeignKey(
        'Thread',
        on_delete=models.PROTECT,
        related_name='thread',
        editable=False
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'thread_items'

    def __str__(self):
        return 'ThreadItem (' + self.thread_item_id + ')'
