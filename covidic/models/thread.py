from django.db import models


class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)

    create_user = models.ForeignKey(
        'account_manager.Account',
        on_delete=models.SET_NULL,
        null=True,
        editable=False
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'threads'

    def __str__(self):
        return 'Thread (' + self.thread_id + ') ' + self.title
