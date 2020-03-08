from django.db import models


class TimelineAccident(models.Model):
    accident_id = models.AutoField(primary_key=True)
    ACCIDENT_TYPES = [
        ('M', '의료진 감염'),
        ('N', '국가위생건강위원회 기록'),
        ('C', '후베이와 우한의 중앙회의'),
        ('I', '국제 피드백'),
        ('T', '국면 전환점'),
    ]

    typeof = models.CharField(max_length=1, choices=ACCIDENT_TYPES)
    title = models.CharField(max_length=128)
    link = models.URLField(max_length=200)

    class Meta:
        db_table = 'timeline_accidents'
        unique_together = ['typeof', 'title']
