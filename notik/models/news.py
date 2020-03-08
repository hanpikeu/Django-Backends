from django.db import models


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=128)
    reaction = models.IntegerField(default=0)

    class Meta:
        db_table = 'newses'
        unique_together = ['link']
