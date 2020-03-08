import uuid

from django.db import models


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    discord_id = models.BigIntegerField()
    is_able = models.BooleanField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    token = models.UUIDField(default=uuid.uuid1)
    token_create_time = models.DateTimeField()

    class Meta:
        db_table = 'accounts'
        unique_together = ['discord_id']


class TimelineDate(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField()

    class Meta:
        db_table = 'timeline_dates'
        unique_together = ['date']


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


class TagOfArchive(models.Model):
    tag_of_archive_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'tags_of_archive'
        unique_together = ['name']


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


class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)

    create_user = models.ForeignKey(
        'Account',
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts"
    )
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'threads'


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


class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    link = models.URLField(max_length=200)
    title = models.CharField(max_length=128)
    reaction = models.IntegerField(default=0)

    class Meta:
        db_table = 'newses'
        unique_together = ['link']


class NewsComments(models.Model):
    link = models.URLField(max_length=200)
    writer_id = models.CharField(max_length=128)
    content = models.CharField(max_length=200)
    hand_up = models.IntegerField(default=0)
    hand_down = models.IntegerField(default=0)
    reaction = models.IntegerField(default=0)

    class Meta:
        db_table = 'news_comments'
