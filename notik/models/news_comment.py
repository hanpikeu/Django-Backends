from django.db import models


class NewsComments(models.Model):
    link = models.URLField(max_length=200)
    writer_id = models.CharField(max_length=128)
    content = models.CharField(max_length=200)
    hand_up = models.IntegerField(default=0)
    hand_down = models.IntegerField(default=0)

    class Meta:
        db_table = 'news_comments'
