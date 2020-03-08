# Generated by Django 3.0.4 on 2020-03-08 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('typeof', models.CharField(choices=[('I', 'IMGUR'), ('A', 'ARCHIVE')], max_length=1)),
                ('archive_id', models.AutoField(primary_key=True, serialize=False)),
                ('tags', models.TextField()),
                ('link', models.URLField()),
            ],
            options={
                'db_table': 'archives',
                'unique_together': {('link',)},
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('typeof', models.CharField(choices=[('A-N', 'Add news'), ('A-T', 'Add timeline'), ('U-T', 'Update timeline'), ('TC-', 'Token Create'), ('A-C', 'Archive Create'), ('T-C', 'Thread Create'), ('TIC', 'Thread Item Create'), ('ATC', 'Archive Tag Change')], max_length=3)),
                ('desc', models.CharField(max_length=255)),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('log_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'logs',
            },
        ),
        migrations.CreateModel(
            name='TimelineDate',
            fields=[
                ('date_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'timeline_dates',
                'unique_together': {('date',)},
            },
        ),
        migrations.CreateModel(
            name='TimelineAccident',
            fields=[
                ('accident_id', models.AutoField(primary_key=True, serialize=False)),
                ('typeof', models.CharField(choices=[('M', '의료진 감염'), ('N', '국가위생건강위원회 기록'), ('C', '후베이와 우한의 중앙회의'), ('I', '국제 피드백'), ('T', '국면 전환점')], max_length=1)),
                ('title', models.CharField(max_length=128)),
                ('link', models.URLField()),
            ],
            options={
                'db_table': 'timeline_accidents',
                'unique_together': {('typeof', 'title')},
            },
        ),
        migrations.CreateModel(
            name='ThreadItem',
            fields=[
                ('thread_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='references',
                                              to='covidic.Archive')),
            ],
            options={
                'db_table': 'thread_items',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('thread_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('create_user',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts',
                                   to='account_manager.Account')),
            ],
            options={
                'db_table': 'threads',
            },
        ),
        migrations.CreateModel(
            name='TagOfArchive',
            fields=[
                ('tag_of_archive_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'tags_of_archive',
                'unique_together': {('name',)},
            },
        ),
    ]
