# Generated by Django 3.0.4 on 2020-03-15 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField()),
                ('writer_id', models.CharField(max_length=128)),
                ('content', models.CharField(max_length=200)),
                ('hand_up', models.IntegerField(default=0)),
                ('hand_down', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'news_comments',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=128)),
                ('reaction', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'newses',
                'unique_together': {('link',)},
            },
        ),
    ]
