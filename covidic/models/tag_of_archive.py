from django.db import models


class TagOfArchive(models.Model):
    tag_of_archive_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'tags_of_archive'
        unique_together = ['name']
