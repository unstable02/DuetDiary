# Generated by Django 5.1.5 on 2025-03-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='uploader',
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='Untitled Song', max_length=255),
        ),
    ]
