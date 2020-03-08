from django.db import models


class Log(models.Model):
    LOG_TYPE = [
        ('A-N', 'Add news'),
        ('A-T', 'Add timeline'),
        ('U-T', 'Update timeline'),
        ('TC-', 'Token Create'),
        ('A-C', 'Archive Create'),
        ('T-C', 'Thread Create'),
        ('TIC', 'Thread Item Create'),
        ('ATC', 'Archive Tag Change'),
    ]

    typeof = models.CharField(max_length=3, choices=LOG_TYPE)
    desc = models.CharField(max_length=255)
    log_time = models.DateTimeField(auto_now_add=True)
    log_id = models.AutoField(primary_key=True)

    class Meta:
        db_table = 'logs'
