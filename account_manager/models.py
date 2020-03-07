from django.db import models

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    discord_userid = models.BigIntegerField()
    is_able = models.BooleanField()

    created_time = models.DateTimeField(auto_now_add=True)
    modified_time= models.DateTimeField(auto_now=True)
    
    token = models.CharField(max_length=36)
    token_create_time = models.DateTimeField()

    class Meta:
        db_table = 'accounts'

class TimelineDate(models.Model):
    date_id = models.AutoField(primary_key=True)
    date = models.DateField()

    class Meta:
        db_table = 'timeline_dates'

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
    link = models.CharField(max_length=1024)

    class Meta:
        db_table = 'timeline_accidents'

class TagOfArhive(models.Model):
    tag_of_arhive_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        db_table = 'tags_of_arhive'

class Arhive(models.Model):
    ACHIVE_TYPE = [
        ('I', 'IMGUR'),
        ('A', 'ARHIVE'),
    ]
    typeof = models.CharField(max_length=1, choices=ACHIVE_TYPE)
    arhive_id = models.AutoField(primary_key=True)
    tags = models.TextField()

    class Meta:
        db_table = 'arhives'

class Thread(models.Model):
    thread_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    
    create_user = models.ForeignKey(
        'Account',
        on_delete = models.SET_NULL,
        null = True,
    )
    created_time  = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'threads'

class ThreadItem(models.Model):
    thread_item_id = models.AutoField(primary_key=True)

    content = models.ForeignKey(
        'Arhive',
        on_delete = models.PROTECT
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
            ('A-C', 'Arhive Create'),
            ('T-C', 'Thread Create'),
            ('TIC', 'Thread Item Create'),
            ('ATC', 'Arhive Tag Chanage'),
    ]

    typeof = models.CharField(max_length=3, choices=LOG_TYPE)
    desc = models.CharField(max_length=255)
    log_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'logs'

class News(models.Model):
    news_id = models.AutoField(primary_key=True)
    link = models.CharField(max_length=1024)
    title = models.CharField(max_length=128)
    
    class Meta:
        db_table = 'newses'
