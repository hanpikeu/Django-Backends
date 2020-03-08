from django.db import models


class ThreadItem(models.Model):
    thread_item_id = models.AutoField(primary_key=True)

    content = models.ForeignKey(
        'Archive',
        on_delete=models.PROTECT,
        related_name='references'
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'thread_items'
