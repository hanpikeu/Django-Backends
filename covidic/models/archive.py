from django.db import models


class Archive(models.Model):
    ARCHIVE_TYPE = [
        ('I', 'IMGUR'),
        ('A', 'ARCHIVE'),
    ]
    typeof = models.CharField(max_length=1, choices=ARCHIVE_TYPE)
    archive_id = models.AutoField(primary_key=True)
    tags = models.TextField()
    link = models.URLField(max_length=200)

    class Meta:
        db_table = 'archives'
        unique_together = ['link']

    def __str__(self):
        return 'Archive (' + self.archive_id + ') ' + self.link
