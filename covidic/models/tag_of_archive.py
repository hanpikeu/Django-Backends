from django.db import models


class TagOfArchive(models.Model):
    tag_of_archive_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, editable=False)
    desc = models.CharField(max_length=255)

    class Meta:
        db_table = 'tags_of_archive'
        unique_together = ['name']

    def __str__(self):
        return 'TagOfArchive (' + self.tag_of_archive_id + ') ' + self.name
